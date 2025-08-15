todos = []

print("ToDoApp, (add,remove,show,exit)")

while True:
    cmd = input("> ").strip()
    
    if cmd == "exit":
        print("終了")
        break
    
    elif cmd == "show":
        if not todos:
            print("(カラです)")
        else:
            for i, task in enumerate(todos, start=1):
                print(f"{i}. {task}")
                
    elif cmd.startswith("add "):
        task = cmd[4:].strip()
        if task:
            todos.append(task)
            print(f"追加:{task}")
        else:
            print("追加する内容を書いてね（例：add 牛乳を買う)")
            
    elif cmd.startswith("remove "):
        num_str = cmd[7:].strip()
        if num_str.isdigit():
            i = int(num_str) - 1
            if 0 <= i < len(todos):
                removed = todos.pop(i)
                print(f"削除： {removed}")
            else:
                print("there is no number")
        else:            
            print("削除する番号を数字で指定してね（例： remove 1)")
    else:
        print("使い方： add<内容> / remove <番号> / show / exit")