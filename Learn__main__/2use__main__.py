from matplotlib import cm
import use__main__


print (f"Second Module's Name: {__name__}")

print("Ingrese a o b")

cmd = input()
cmd = cmd.lower()

if cmd == "a":
    use__main__.main()
elif cmd == "b":
    use__main__.suma()
else:
    print("intente de nuevo")

print("alles gut")