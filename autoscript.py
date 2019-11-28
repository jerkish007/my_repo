from pywinauto.application import Application
app = Application().start("notepad.exe")
app.UntitledNotepad.Edit.type_keys("Hello i am giving demo for automation testing, and the script is written in python with the use of pywinauto library. So this has following steps that will take place. And now i m going to write the steps to see when i run this script will it place the steps similarly of diffrently. So steps are: 1. Opening a new notepad. 2. Writing a short data. 3. Saving Aa the file.", with_spaces =True)
app.UntitledNotepad.menu_select("File->SaveAs")
app.SaveAs.exit1.set_text("Tst_pywinauto.txt")
app.SaveAs.Save.click()
app.Tst_pywinauto.close()
