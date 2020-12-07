## Exercise 1 (Name Generator)

Ade is a database engineer, he created a database table named `user` that has three columns namely `first_name, last_name and full_name(a combination of first_name and last_name)`. 

Ade needs 5 random names to be seeded into this database. It takes him a quality amount of time to think, type and insert these names into his database, he thinks this task can be automated.

Ade consulted you as a software engineer to create an automation tool that will generate 5 names with some constraints so he can populate his data with ease.

Write a simple function named `name_generator` that takes in vowels and consonants letters as an argument, that will generate five (5) random names from the combination of vowel and consonant letters passed as an argument with the following constraints.

- Name generated for each first_name and last_name is not less than 3 characters
- Name generated for first_name must start with Vowel letter
- Name generated for last_name must start with Consonant letter
- Validate that the vowel argument only comprises of vowel letters and consonant argument only comprises of consonants letters

Note: make sure you raise an exception with a meaningful error message if the validation fails.

Expected output

```python
[
  {
    first_name: “Essien”,
    last_name: “Doe”,
    full_name: “Essien Doe”
  },
  {
    first_name: “Adckwt”,
    last_name: “Kadbsdu”,
    full_name: “Adckwt Kadbsdu”
  },
...
]
`
```