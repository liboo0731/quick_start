package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	//打印当前文件绝对路径
	fmt.Println(os.Args[0])
	fmt.Println(filepath.Abs(filepath.Dir(os.Args[0])))
	//创建临时目录
	tempDir, _ := ioutil.TempDir(".", "tmpdio")
	//切换工作路径
	os.Chdir(tempDir)
	//打印当前路径
	fmt.Println(os.Getwd())
	//创建目录
	os.Mkdir("aaa", 0755)
	//创建多级目录
	os.MkdirAll("aaa/bb/cc", 0755)
	//创建临时目录
	os.MkdirTemp(".", "tmpdos")
	//创建临时文件
	tempFile, _ := ioutil.TempFile(".", "tmpfio")
	//读写文件
	//os.Open()
	openFile, _ := os.OpenFile(tempFile.Name(), os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	openFile.WriteString("hello world")
	io.WriteString(openFile, "hi,tim")
	readAll, _ := ioutil.ReadAll(openFile)
	fmt.Printf("open: %s\n", string(readAll))
	//拷贝文件
	if _, err := os.Stat(tempFile.Name()); !os.IsNotExist(err) {
		copyFile, _ := os.Create("copyfile")
		io.Copy(openFile, copyFile)
		fmt.Println("copy end")
	}
	openFile.Close()
	bytes, _ := ioutil.ReadFile(tempFile.Name())
	fmt.Printf("io: %s\n", string(bytes))
	pdir, _ := filepath.Abs(tempDir)
	fmt.Printf("tempdir:%s\n", tempDir)
	fmt.Printf("absdir:%s\n", pdir)
	fmt.Printf("dir:%s\n", filepath.Dir(filepath.Dir(pdir)))
	os.Chdir("../")
	fmt.Println(os.Getwd())
	//遍历当前目录
	currDir, _ := ioutil.ReadDir(".")
	for _, subItem := range currDir {
		if subItem.IsDir() {
			//创建文件
			os.Create("foo")
			//前缀匹配
			if strings.HasPrefix(subItem.Name(), "tmp") {
				fmt.Println(subItem.Name())
				fmt.Println(os.Getwd())
				//删除空目录或者文件
				os.Remove(subItem.Name())
				//路径删除
				os.RemoveAll(subItem.Name())
			}
			//后缀匹配
			if strings.HasSuffix(subItem.Name(), "tmp") {
				fmt.Println(subItem.Name())
			}
		} else {
			//移动文件
			os.Rename(filepath.Join(tempDir, subItem.Name()),
				filepath.Join(tempDir, fmt.Sprintf("re%s", subItem.Name())))
		}
	}
	//获取当前目录对象数量，可用于判断目录是否为空
	fmt.Println(len(currDir))
}
