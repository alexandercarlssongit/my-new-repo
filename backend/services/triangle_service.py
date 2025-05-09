import math
from dataclasses import dataclass
from typing import Tuple, List

@dataclass
class TriangleResult:
    is_triangle: bool
    triangle_type: str
    angles: Tuple[float, float, float]
    area: float
    perimeter: float

class TriangleService:
    @staticmethod
    def is_valid_triangle(side1: float, side2: float, side3: float) -> bool:
        """Check if three sides can form a triangle using the triangle inequality theorem."""
        return (side1 + side2 > side3 and 
                side2 + side3 > side1 and 
                side1 + side3 > side2)

    @staticmethod
    def calculate_angles(side1: float, side2: float, side3: float) -> Tuple[float, float, float]:
        """Calculate the angles of a triangle using the law of cosines."""
        # Law of cosines: c² = a² + b² - 2ab cos(C)
        angle1 = math.degrees(math.acos((side2**2 + side3**2 - side1**2) / (2 * side2 * side3)))
        angle2 = math.degrees(math.acos((side1**2 + side3**2 - side2**2) / (2 * side1 * side3)))
        angle3 = math.degrees(math.acos((side1**2 + side2**2 - side3**2) / (2 * side1 * side2)))
        return (angle1, angle2, angle3)

    @staticmethod
    def calculate_area(side1: float, side2: float, side3: float) -> float:
        """Calculate the area of a triangle using Heron's formula."""
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    @staticmethod
    def determine_triangle_type(side1: float, side2: float, side3: float, angles: Tuple[float, float, float]) -> str:
        """Determine the type of triangle based on sides and angles."""
        types = []
        
        # Check side-based types
        if side1 == side2 == side3:
            types.append("Equilateral")
        elif side1 == side2 or side2 == side3 or side1 == side3:
            types.append("Isosceles")
        else:
            types.append("Scalene")
            
        # Check angle-based types
        if any(abs(angle - 90) < 0.001 for angle in angles):
            types.append("Right")
        elif all(angle < 90 for angle in angles):
            types.append("Acute")
        else:
            types.append("Obtuse")
            
        return " ".join(types)

    def analyze_triangle(self, side1: float, side2: float, side3: float) -> TriangleResult:
        """Analyze a triangle and return its properties."""
        if not self.is_valid_triangle(side1, side2, side3):
            return TriangleResult(
                is_triangle=False,
                triangle_type="Not a triangle",
                angles=(0, 0, 0),
                area=0,
                perimeter=0
            )

        angles = self.calculate_angles(side1, side2, side3)
        triangle_type = self.determine_triangle_type(side1, side2, side3, angles)
        area = self.calculate_area(side1, side2, side3)
        perimeter = side1 + side2 + side3

        return TriangleResult(
            is_triangle=True,
            triangle_type=triangle_type,
            angles=angles,
            area=area,
            perimeter=perimeter
        ) 