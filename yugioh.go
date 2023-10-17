package main

//	-------------------
//	|     Imports     |
//	-------------------

import (
	"os"
	"fmt"
	"bufio"
	"strings"
	"strconv"
	"os/user"
	"runtime"
)

//	----------------------------
//	|     Type Definitions     |
//	----------------------------

type Player struct {
	name		string
	lifepoints	int
}

//	-------------------------
//	|     File Handling     |
//	-------------------------

func CreateFileDirectory(directory string) {

}

func GetFilePath() string {
	os			:= runtime.GOOS
	user, err	:= user.Current()
	if err != nil { return "" }

	switch os {
		case "linux":	return fmt.Sprintf("/home/%s/.config/yugioh/stats.csv", user.Username)
		case "darwin":	return fmt.Sprintf("/Users/%s/.config/yugioh/stats.csv", user.Username)
		default:		return ""
	}
}

func WriteStats(players *[]Player) {
	panic("WriteStats(players *[]Player) { ... } is not yet implemented properly")

	file, err := os.OpenFile(GetFilePath(), os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil { fmt.Println("Error opening file: ", err) ; os.Exit(1) }
	defer file.Close()

	data	:= fmt.Sprintf("%s,%d,%s,%d\n",
			(*players)[0].name, (*players)[0].lifepoints, (*players)[1].name, (*players)[1].lifepoints)

	_, err = file.WriteString(data)
	if err != nil { fmt.Println("Error writing to file: ", err) ; os.Exit(1) }

	os.Exit(0)
}

//	----------------------------
//	|     Command Handling     |
//	----------------------------

func ParseCommand(players *[]Player, command string) {
	commands := strings.Split(command, " ")

	if commands[0] == "exit" { os.Exit(0) }
	if len(commands) != 3 { return }

	index, err	:= strconv.Atoi(commands[0])
	if err != nil || index >= 2 { return }
	points, err	:= strconv.Atoi(commands[2])
	if err != nil { return }
	symbol	:= commands[1]

	switch symbol {
		case "-":	(*players)[index].lifepoints -= points
		case "+":	(*players)[index].lifepoints += points
	}
}

//	------------------
//	|    Visuals     |
//	------------------

func Logo() {
	fmt.Print("\u001b[0;0H\u001b[2J\u001b[1;36m")
	fmt.Println(`__   __      ____ _  ___  _     _ `)
	fmt.Println(`\ \ / /   _ / ___(_)/ _ \| |__ | |`)
	fmt.Println(` \ V / | | | |  _| | | | | '_ \| |`)
	fmt.Println(`  | || |_| | |_| | | |_| | | | |_|`)
	fmt.Println(`  |_| \__,_|\____|_|\___/|_| |_(_) (in Go)`)
	fmt.Println("\u001b[0m")
}

func Prompt(players *[]Player) {
	Logo()
	for index, player := range (*players) {
		formatBuffer := ""
		for i := 0; i < 12 - len(player.name); i++ { formatBuffer += " " }
		fmt.Println(fmt.Sprintf("\u001b[1m[%d] \u001b[32m%s:%s\u001b[0m%d",
				index, player.name, formatBuffer, player.lifepoints))
	}

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("\u001b[1m>> \u001b[0m")
	command, err := reader.ReadString('\n')
	if err == nil { ParseCommand(players, strings.TrimSpace(command)) }
}

//	----------------------
//	|    Entry Point     |
//	----------------------

func main() {
	players := []Player{}

	for index, item := range os.Args {
		if index == 0 { continue }
		if index >= 3 { break }
		players = append(players, Player{item,8000})
	}

	for true {
		Prompt(&players)
		for _, player := range players { if player.lifepoints <= 0 { WriteStats(&players) } }
	}
}
