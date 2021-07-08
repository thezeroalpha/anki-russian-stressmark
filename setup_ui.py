from aqt.editor import Editor
from anki.hooks import addHook
import os
import json
from .russiangram_requests import stressmark

def stressmarkSelection(editor) -> None:
    selected = editor.web.selectedText()
    if selected:
        editor.web.eval(""" document.execCommand("insertHTML", false, %s); """ % json.dumps(stressmark(selected)))

def addButton(buttons, editor):
    tt = "Add Stress Marks"
    icon_name = "add.png"
    icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons"), icon_name)
    b = editor.addButton(icon, "STRESSMARK", stressmarkSelection, tip=_("{}".format(tt)))
    buttons.append(b)
    return buttons

addHook('setupEditorButtons', addButton)
