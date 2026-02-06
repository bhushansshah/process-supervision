from datasets import load_dataset
# load the dataset
ds = load_dataset("KbsdJames/Omni-MATH")

# print the dataset
print(ds)

# print the first example
print(ds['test'][0])

# print the fields of the dataset
print(ds['test'].column_names)

# print the length of the dataset
print(len(ds['test']))

# save the dataset to the data folder
ds.save_to_disk("./data/omni_math")