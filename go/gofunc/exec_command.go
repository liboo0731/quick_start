package main

import (
	"bufio"
	"fmt"
	"io"
	"os/exec"
)

func syncPrint(out io.ReadCloser) {
	in := bufio.NewScanner(out)
	for in.Scan() {
		fmt.Println(string(in.Bytes()))
	}
}

func main() {
	exeCmd := "ls"
	cmd := exec.Command("bash", "-c", exeCmd)
	stdout, _ := cmd.StdoutPipe()
	stderr, _ := cmd.StderrPipe()
	cmd.Start()
	go syncPrint(stdout)
	go syncPrint(stderr)
	cmd.Wait()
}
