import math

def main():
    trignometry()
    
    
def trignometry():
    angle_degrees = float(input("Enter angle in degrees: "))
    angle_radian = math.radians(angle_degrees)
    
    sine = math.sin(angle_radian)
    cosine = math.cos(angle_radian)
    tangent = math.tan(angle_radian)
    
    print(f"Sine: {sine}")
    print(f"Cosine: {cosine}")
    print(f"Tangent: {tangent}")
    
    
if __name__ == "__main__":
    main()


    