import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import requests
import yaml
import os
import sys
from datetime import datetime

# Load configuration
with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

API_URL = f"http://{config['server']['host']}:{config['server']['port']}{config['server']['api_prefix']}/triangle"

def draw_triangle(side1, side2, side3, is_triangle):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    if not is_triangle:
        # Draw red X
        ax.plot([0, 1], [0, 1], 'r-', linewidth=2)
        ax.plot([0, 1], [1, 0], 'r-', linewidth=2)
        ax.set_xlim(-0.1, 1.1)
        ax.set_ylim(-0.1, 1.1)
    else:
        # Calculate triangle coordinates
        # Using the law of cosines to find the third point
        angle = np.arccos((side1**2 + side2**2 - side3**2) / (2 * side1 * side2))
        
        # Scale the triangle to fit in the plot
        scale = 5 / max(side1, side2, side3)
        side1 *= scale
        side2 *= scale
        side3 *= scale
        
        # Calculate coordinates
        x = [0, side1, side2 * np.cos(angle)]
        y = [0, 0, side2 * np.sin(angle)]
        
        # Draw triangle
        ax.plot([x[0], x[1]], [y[0], y[1]], 'b-', linewidth=2)
        ax.plot([x[1], x[2]], [y[1], y[2]], 'b-', linewidth=2)
        ax.plot([x[2], x[0]], [y[2], y[0]], 'b-', linewidth=2)
        
        # Add side lengths
        ax.text((x[0] + x[1])/2, (y[0] + y[1])/2 - 0.2, f'{side1/scale:.1f}', ha='center')
        ax.text((x[1] + x[2])/2, (y[1] + y[2])/2, f'{side2/scale:.1f}', ha='center')
        ax.text((x[2] + x[0])/2, (y[2] + y[0])/2, f'{side3/scale:.1f}', ha='center')
        
        # Set equal aspect ratio and remove axes
        ax.set_aspect('equal')
        ax.axis('off')
    
    return fig

def main():
    st.title("Triangle Calculator")
    
    # Input form
    with st.form("triangle_form"):
        username = st.text_input("Your Name")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            side1 = st.number_input("Side 1", min_value=0.0, value=3.0)
        with col2:
            side2 = st.number_input("Side 2", min_value=0.0, value=4.0)
        with col3:
            side3 = st.number_input("Side 3", min_value=0.0, value=5.0)
        
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        try:
            # Call API
            response = requests.post(API_URL, json={
                'username': username,
                'side1': side1,
                'side2': side2,
                'side3': side3
            })
            result = response.json()
            
            # Display results
            st.subheader("Results")
            
            # Draw triangle
            fig = draw_triangle(side1, side2, side3, result['is_triangle'])
            st.pyplot(fig)
            
            # Display triangle properties
            if result['is_triangle']:
                st.success(f"Type: {result['triangle_type']}")
                st.write(f"Angles: {', '.join(f'{angle:.1f}°' for angle in result['angles'])}")
                st.write(f"Area: {result['area']:.2f} square units")
                st.write(f"Perimeter: {result['perimeter']:.2f} units")
            else:
                st.error("These sides cannot form a triangle!")
                
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 