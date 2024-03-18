from latex_generator import latex_generator

def save_to_tex_file(data):
    latex_data = latex_generator.generate_latex_table(data)
    with open('artifacts/output.tex', 'w') as file:
        # Write the LaTeX content to the file
        file.write(latex_data)
    latex_data = latex_generator.generate_latex_img('artifacts/image.png')
    with open('artifacts/output2.tex', 'w') as file:
        # Write the LaTeX content to the file
        file.write(latex_data)


if __name__=='__main__':
    data = [
        ["Natan", 30, "Java-developer"],
        ["Narendra", 25, "PM"],
        ["Alex", 35, "C++-developer"]
    ]
    save_to_tex_file(data)
