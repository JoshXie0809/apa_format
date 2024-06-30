import sys

## process paper's author to apa format
def author_process(author_str):
    authors = author_str.split(" and")
    ret = ""
    n = len(authors)
    for i, author in enumerate(authors):
        first_comma = False
        for letter in author:
            if not first_comma:
                ret += letter
            
            if letter == ",": 
                first_comma = True
                ret += " "
            
            if first_comma & letter.isupper():
                ret += letter + ". "
        
        if i + 1 < n - 1:
            ret = ret[:-1]
            ret += ","
        elif i + 1 == n - 1:
            ret += "\\&"
    
    return ret

## a paper's final result (in tex)
def apa_tex(p_dict):
    author_str = author_process(p_dict["author"])
    year_str = p_dict["year"].replace(",", "")
    title_str = p_dict["title"].replace(",", "")
    if title_str[-1] not in ["!", "?", "."]: title_str += "."
    ret =  f"\\laref {author_str}({year_str}). {title_str}"

    if "journal" in p_dict.keys():
        journal_str = p_dict["journal"].replace(",", "")
        ret = f"{ret} {{\\it {journal_str}}}"

        if "volume" in p_dict.keys():
            volumn_str = p_dict["volume"].replace(",", "")
            ret = f"{ret}, {volumn_str}"
        if "number" in p_dict.keys():
            number_str = p_dict["number"].replace(",", "")
            ret = f"{ret}({number_str})"
        if "pages" in p_dict.keys():
            pages_str = p_dict["pages"].replace(",", "")
            ret = f"{ret}, {pages_str}."
    
    if ret[-1] != ".": ret += '.'
    return ret

def transform_google_scholar_bibtext(file, target_file):
   
    ## read bibfile
    with open(file, "r") as f:
        lines = f.readlines()
    
    ## collect papers: string
    papers = []
    first = False
    for line in lines:
        if "@" in line:
            if first:
                papers.append(paper)
            paper = ""
            first = True
        if line != "\n":
            paper += line
    ## add final paper
    papers.append(paper)

    ## collect papers: process field
    papers_dict = []
    for i in range(len(papers)):
        p_dict = {}
        a = papers[i].split("\n")
        for j in a:
            if "=" in j:
                res = j.split("=")
                k = res[0].replace(" ", "")
                v = res[1]
                if v[-1] == ",":
                    v = v[:-1]
                v = v[1:(-1)]
                p_dict[k] = v
        papers_dict.append(p_dict)

    ## write file
    with open(target_file, "+w", encoding="utf8") as f:
        for p_dict in papers_dict:
            f.write(apa_tex(p_dict))
            f.write("\n\n")

def main():
    if len(sys.argv[1:]) != 2:
        print("Usage: needs bibfile's path and output.txt's path")
        return 
    
    # print bibfile's path
    print(f"bibfile path: {sys.argv[1]}")
    print(f"output  path: {sys.argv[2]}")

    # file = "./bibfile.bib or /bibfile.txt"
    # target = "res.txt"

    transform_google_scholar_bibtext(
        file = sys.argv[1],   
        target_file = sys.argv[2]
    )

    print("transform completed.")

if __name__ == "__main__":
    main()

