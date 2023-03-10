# CSV Combiner

Write a command line program that takes several CSV files as arguments. Each CSV
file (found in the `fixtures` directory of this repo) will have the same
columns. Your script should output a new CSV file to `stdout` that contains the
rows from each of the inputs along with an additional column that has the
filename from which the row came (only the file's basename, not the entire path).
Use `filename` as the header for the additional column.

##  Considerations
* You should use coding best practices. Your code should be re-usable and extensible.
* Your code should be testable by a CI/CD process. 
* Unit tests should be included.

## Usage

the user can input many different files to combine, and the last argument must be the name of the output file where all the input files will be combined

Examples:

Given three input files named `accessories.csv`, `clothing.csv` and `household_cleaner.csv`. and an output file `result.csv`

```
$ python3 results.py accessories.csv clothing.csv household_cleaners.csv result.csv
```

Given two input files named `accessories.csv` and `clothing.csv`  and an output file `result.csv`

```
$ python3 results.py accessories.csv clothing.csv result.csv
```

# pmgChallenge
