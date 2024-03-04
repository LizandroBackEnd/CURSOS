from pathlib import Path 

file = Path("files/file_test.txt") 
text = file.read_text("utf-8").split("\n") 
text.insert(0, "Insert text in this line") 
file.write_text("\n".join(text), "utf-8")
 
