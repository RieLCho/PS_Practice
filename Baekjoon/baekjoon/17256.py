a_x, a_y, a_z = map(int, input().split())
c_x, c_y, c_z = map(int, input().split())

# a 🍰 b = (a.z + b.x, a.y × b.y, a.x + b.z)

print(c_x - a_z, round(c_y / a_y), c_z - a_x)