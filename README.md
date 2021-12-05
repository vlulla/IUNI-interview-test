---
title: IUNI interview assignment
geometry: "margin=1in"
...

# The task

Convert the provided log file into the following format:

Log message | Start Time | End Time | Time Diff
------------|------------|----------|----------
timeline ep starts - timeline ep ends | 2021-07-21 21:47:45.588 | 2021-07-21 21:48:48.423 | 1.03333
network EP starts - network EP ends | 2021-07-21 21:48:49.160 | 2021-07-21 21:49:51.988 | 1.03333
Article api starts - article api ends | 2021-07-21 21:51:19.742 | 2021-07-21 21:51:21.734 | 0.01666


The first few lines from the provided log file are:

```
2021-08-02 12:18:54,549 templogger   WARNING  "d9729770-87a6-452d-a8d2-c3f7dc354db8" "Articles api starts"
2021-08-02 12:18:56,841 templogger   WARNING  "d9729770-87a6-452d-a8d2-c3f7dc354db8" "Articles api ends"
2021-08-02 12:18:57,659 templogger   WARNING  "52a419df-696f-49c7-b6ee-0005c7e50e4d" "network EP starts"
2021-08-02 12:18:57,659 templogger   WARNING  "50dd359b-faa2-45d5-b2d2-51fb4892179f" "timeline ep starts"
```

# Solution

The `parselog.py` script will convert, almost, the provided log file into the required output format. The script can be 
run on the command line as `python parselog.py`[^python-interactive-after-script] or can be imported into a repl using `import parselog` 
with python started in the current directory.

Put the script in the same folder where the `api.log` is located. Then you can run the following command to generate the csv:

```bash
$ python parselog.py > output.csv
```

Or you can also explore the script in an interactive session. Here's an example:

```python
>>> import parselog as p
>>> dir(P)
>>> help(p.getLogLines)
>>> p.main("api.log")
```

## Some shortcomings of this script

- The `Time Diff` column is incorrect! I could not figure out how to generate
  the difference listed in the provided example.
- The script is missing error checking and very task specific! I believe this
  script will run into issues if the unique ID column (fifth column) has
  embedded spaces in it!
- Documentation is lacking! I didn't put much effort into documentation because
  I believe that the script is not general enough to have functions/classes
  that can be used beyond the current task. Therefore, I did not put much
  effort into documenting the functions.
- The script is missing tests!

[^python-interactive-after-script]: Calling Python with `-i` switch will start an `interactive` prompt after the script is run!
