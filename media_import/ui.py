from .dialog import ImportDialog

import_dialog: ImportDialog = None


def open_import_dialog() -> None:

    global import_dialog
    if import_dialog is None:
        import_dialog = ImportDialog()
    if not import_dialog.isVisible():
        import_dialog.show()
    import_dialog.activateWindow()
    import_dialog.raise_()
