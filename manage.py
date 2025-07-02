import Project

def main():
    try:
        # Project.exe,
        Project.project.run(debug= True)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()