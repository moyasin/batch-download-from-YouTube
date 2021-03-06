import os

class FileManager():
    def __init__(self,dir=""):
        self.home_dir = dir

    def make_unique_dir(self,name=""):
        dir_name = name
        # 新規ディレクトが作成されるまでループ
        while(True):
            # ディレクトリ名を標準入力
            if name == "":
                dir_name=input("Enter directory name, ex:test/sample")
            dir_name = self.home_dir + "/" + dir_name

            # ディレクトリ名に重複がない場合
            try:
                # ディレクトリを作成
                os.mkdir(dir_name)
                print("make:",dir_name)
                # ループを抜ける
                break

            # ディレクトリ名が重複している場合
            except FileExistsError:
                print("Sorry, the directory is exist")

            # ディレクトリの親ディレクトリが存在しない場合
            except FileNotFoundError:
                # 入力をディレクトリごとに分割する
                dir_name_list = dir_name.split("/")
                process = ""

                # 親ディレクトリから順番に作成する
                for dir_ in dir_name_list:
                    # ここまでのディレクトパスを結合
                    process = os.path.join(process,dir_)

                    # ディレクトリが存在しない場合
                    try:
                        os.mkdir(process)
                        print("make:",process)

                    # ディレクトが存在する場合
                    except FileExistsError:
                        pass
                break

        return dir_name

if __name__ == "__main__":
    home_dir = input("input home directory : ")
    fm = FileManager(home_dir)
    fm.make_unique_dir()
