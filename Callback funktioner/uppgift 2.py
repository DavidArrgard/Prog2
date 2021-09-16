def food(s, vegan=False):
    if vegan:
        print("sojamjölk")
    else:
        print("mjölk")


food("mjölk")       # mjölk
food("mjölk", True)  # sojamjölk
