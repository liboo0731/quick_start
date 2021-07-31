### Linux问题处理思路

1. ipcs/ipcrm 用户uid变更，文件/文件夹权限显示原有uid，信号量占用
2. lseek或truncate到一个固定位置生成的“空洞文件”是不会占据真正的磁盘空间
3. fallocate快速的为某个文件分配实际的磁盘空间，主流文件系统如ext4，xfs支持
4. dd用于测试硬盘读写，数据备份恢复，指定大小的块拷贝一个文件，并在拷贝的同时进行指定的转换
5. lsof查询处理已经删除文件却没有释放存储空间
6. blkid查询分区UUID
7. lsblk查询磁盘分区使用
8. mount设置文件系统使用参数



### Linux系统配置

1. 路由配置 
2. DNS配置
3. iptables规则查询，配置，删除
4. sshd配置
5. yum，apt镜像源配置



### Linux常用命令

- 解压缩zip，unzip，tar

```bash
# 预览
unzip -v ${zipfile}.zip
unzip -l ${zipfile}.zip
tar -tf ${tarfile}.tar

# 压缩
tar -cvf ${tarfile}.tar ${file}
tar -czvf ${gzfile}.tar.gz ${file}
zip -r ${zipfile}.zip ${file}

# 解压
tar -xvf ${tarfile}.tar
tar -xvf ${gzfile}.tar.gz -C ${destdir}
unzip ${zipfile}.zip -d ${destdir}
```

- 循环执行命令

```bash
for ${item} in $(seq 1 10)
do
	ssh ${ip} "${cmd}"
done
```

- 远程执行本地脚本

```bash
ssh ${ip} "bash" < local.sh
ssh ${ip} "bash -s" < local.sh ${arg1} ${arg2}
```

- 用户切换执行命令

```bash
echo "${param}" |su - ${user} -c "${cmd}"
```

- 敏感信息传递，不在进程中体现

```bash
# $(cat)取值管道，{}取值标准输入
echo "123" |xargs -i echo $(cat) {} <<EOF
234
EOF
# 输出：
# 123 234

# 多行命令
echo "123" |xargs -I {} echo $(cat) {} {} <<EOF
234
345
EOF
# 输出：
# 123 234 234
# 123 345 345
```

- 密钥对生成，互信建立

```bash
# DSA, ECDSA, Ed25519 or RSA
echo "\n" |ssh-keygen -t rsa -P ''
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
```

- 磁盘处理，fdisk，LVM

```bash
# 直接处理磁盘，创建文件系统，后续无法扩展
fdisk -l
fdisk /dev/vdb
# 逻辑卷处理（LVM）pv/vg/lv
# 逻辑卷划分支持百分比，可用于自动化场景
vcreate -l 100%VG -n ${lvname} ${vgname}
# 追加空间
lvextend -l +100%free /dev/${lvname}/${vgname}
resize2fs -p /dev/${lvname}/${vgname}
# 创建文件系统
mkfs.ext4  
```

|      |  物理卷   |   卷组    |  逻辑卷   |
| :--: | :-------: | :-------: | :-------: |
| 扫描 |  pvscan   |  vgscan   |  lvscan   |
| 查看 | pvdisplay | vgdisplay | lvdisplay |
| 查看 |    pvs    |    vgs    |    lvs    |
| 新建 |  pvceate  | vgcreate  | lvcreate  |
| 卸载 | pvremove  | vgremove  | lvremove  |
| 扩展 |     \     | vgextend  | lvextend  |
| 缩容 |     \     | vgreduce  | lvreduce  |

