if __name__ == "__main__":
  try:
    #code you want to run goes here
      with open("test.txt","r") as f: #replace with your file
          lines = f.readlines()
  except:
    #runs if there is an error like FileNotFound
      print("file not found")
