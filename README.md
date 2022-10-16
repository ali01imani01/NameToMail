# NameToMail
Generate Emails for a company/website from a given list of names.


## Usage:
```
git clone https://github.com/ali01imani01/NameToMail.git
cd NameToMail
python3 nametomail.py -f names.txt -d target.tld
```

- You can save your result in a .txt file in terminal like this:

```
python3 nametomail.py -f names.txt -d yahoo.com > output-nametomail.txt

```

- Your `-f any-first-or-last-name-or-both.txt` can be any word (or two words) that you wish. 
But I recommend that use those names that you've found in company's LinkedIn or Crunchbase or theHarvester tool, In order to gain better result.
Your list of names can be something like this:

`$ cat names.txt`
```
cHarLie

liNUS peLt

SNOOPY

sally brown

```

- Don't worry about blank lines, uppercase, lower case names at all! nametomail will take care of them and will give you cool results!:



![nametomail](https://user-images.githubusercontent.com/85396965/196045094-81dccc85-8e87-4bb8-8f90-18f19eef6363.png)

The number of result in our example `names.txt`:

![nametomail2](https://user-images.githubusercontent.com/85396965/196045333-7e5e6b2f-4a7c-48d4-9730-248fc73c205b.png)



- I've also uploaded a `common-names-for-mail.txt` which you can use.

```
python3 nametomail.py -f common-names-for-mail.txt -d yahoo.com > output-nametomail.txt
```

