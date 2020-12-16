You can follow the [Quickstart](index.md) guide or instead follow the next steps to run and test manually:

Clone the project:

```
git clone https://github.com/israteneda/acme
```

Change directory to the app directory:

```
cd acme
```

Run demo:

```
python acme\__main__.py --demo
```

Run custom data:

```
python acme\__main__.py <filename>
```
> Be sure the file is in the same directory where you run the command

Run test:

```
python -m unittest -v
```