# organise-directories-with-python

We can use Python to sort, streamline our files and directories.

Use Python to organise our file directories.

## Code

`pickDirectory()` func:

For-loop to iterate through items in the directory func depending on the file suffix within dictionary. If the function encounters a suffix that doesn't correspond to the four categories defined here, it returns a fifth category, `MISC`, to represent miscellaneous.

To test this function out, call it on .PDF as an example, and print out the result.
`print(pickDirectory(".pdf"))`
Save changes and run the program through the terminal `python3 organize.py`.
As expected, I received 'DOCUMENTS' as the output in terminal because '.pdf' is an item with the list saved inside "DOCUMENTS" keyword prop.

`organizeDirectory()` func:

A for-loop to iterate through each file in the working dir.

If the directory that the file maps to already exists, it skips over the rest of the function body. Otherwise, a file path is created. From that, the file type is extracted. Next, the pickDirectory function that you defined previously is called to assign the correct directory to the current file. Then a directory path is created. If the directory path doesn't already exist, a new directory is created. Finally, the file path is updated to include the new directory path. Call the `organizeDirectory()` to test the program.

Make sure your program is saved within the directory that needs organizing. In this case, the directory is organize_me.

## Testing

`python3 organize_directories_comments.py` # Run the programe.

``

My test has failed and I think its because some of the libraries I've been instructed to install is outdated. I should have x5 new directores (as per the `SUBDIRECTORIES` obj) within the 'organize_me' dir, but I don't. However, I get the picture and now need to move on to the next lecture.
