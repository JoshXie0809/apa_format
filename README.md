# apa_format
transform google scholar bibTeX to apa format using .tex

## usage

```{bash}
python3 transform.py bibfile.txt res.txt
```

terminal shows

```
bibfile path: bibfile.txt
output  path: res.txt
transform completed.
```

## description

copy google scolar's bibTeX format and transfer it to APA format,
sometimes will encounter error when compiling file.tex

`transform.py` transform bibfile to APA(in tex format),
and you can insert the result to Reference in file.tex directly.
