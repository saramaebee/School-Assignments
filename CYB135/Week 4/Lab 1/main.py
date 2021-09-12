def main():
    file_name = input()
    output_dict = {}
    titles = []
    lines = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
    # print(lines)
    for i in range(len(lines)):
        line = lines[i]
        if i % 2 == 0:
            line = int(line[:(len(line)-1)])
            if line not in output_dict:
                output_dict[line] = ''
            else:
                output_dict[line] += '; '
            title = lines[i+1]
            title = title[:(len(title)-1)]
            titles.append(title)
            output_dict[line] += title
    
    with open('output_keys.txt', 'w') as f_keys:
        for key in sorted(output_dict):
            print(f'{key}: {output_dict[key]}', file=f_keys)
            
    with open('output_titles.txt', 'w') as f_titles:
        for title in sorted(titles):
            print(title, file=f_titles)
        
    
if __name__ == "__main__":
    main()
