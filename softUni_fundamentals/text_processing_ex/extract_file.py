file_path = input()
needed_file = file_path.split('\\')[-1]
file_name, file_ext = needed_file.split('.')

print(f'File name: {file_name}')
print(f'File extension: {file_ext}')

"""
tests:
C:\Internal\training-internal\Template.pptx
C:\Projects\Data-Structures\LinkedList.cs
"""