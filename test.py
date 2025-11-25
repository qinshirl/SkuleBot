from langchain_text_splitters.markdown import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["---","\n\n", "\n", " ", ""]
)


with open("result/ESC194F_2022_CALCULUS I_E.md", "r") as f:
    text = f.read()


chunks = splitter.split_text(text)
print(f"生成 {len(chunks)} 个 chunks")
for chunk in chunks:
    print("+++++++++++++++++")
    print(chunk)