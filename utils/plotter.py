import matplotlib.pyplot as plt

def plot_wall(height, top_breadth, base_breadth, weight, active_soil_pressure, passive_soil_pressure, passive_soil_height, lateral_surcharge, water_table, lateral_water):
    fig, ax = plt.subplots()
    wall_polygon = plt.Polygon([[0, 0], [base_breadth, 0], [top_breadth, height], [0, height]], closed=True)
    ax.add_patch(wall_polygon)


    # Add passive soil polygon
    passive_soil_polygon = plt.Polygon([[-base_breadth, 0], [0, 0], [0, passive_soil_height], [-base_breadth, passive_soil_height]], closed=True, alpha=0.5, color='green')
    ax.add_patch(passive_soil_polygon)

    # Arrow scaling factors
    arrow_scale = 0.05
    head_width_scale = 0.1
    head_length_scale = 0.1

    gamma_soil = 18

     # Add active earth pressure triangle
    active_x_loc = base_breadth + 0.5
    active_pressure_triangle = plt.Polygon([[active_x_loc, 0], [active_x_loc, height], [active_x_loc + active_soil_pressure / gamma_soil, 0]], closed=True, alpha=0.3, color='blue', linestyle='--', fill=False)
    ax.add_patch(active_pressure_triangle)

    # Add passive earth pressure triangle
    passive_triangle_height = passive_soil_height - 0.3
    passive_pressure_triangle = plt.Polygon([[0, 0], [-passive_soil_pressure / gamma_soil, 0], [0, passive_triangle_height]], closed=True, alpha=0.3, color='red', linestyle='--', fill=False)
    ax.add_patch(passive_pressure_triangle)

    # Add surcharge pressure
    surcharge_x_loc = active_x_loc + active_soil_pressure / gamma_soil + 1
    surcharge_pressure = plt.Polygon([[surcharge_x_loc, 0], [surcharge_x_loc, height], [surcharge_x_loc + lateral_surcharge / gamma_soil, height], [surcharge_x_loc + lateral_surcharge / gamma_soil, 0]], closed=True, alpha=0.3, color='blue', linestyle='--', fill=False)
    ax.add_patch(surcharge_pressure)

     # Add water pressure triangle
    water_x_loc = surcharge_x_loc + lateral_surcharge/gamma_soil + 1
    water_pressure_triangle = plt.Polygon([[water_x_loc, 0], [water_x_loc, water_table], [water_x_loc + lateral_water / gamma_soil, 0]], closed=True, alpha=0.3, color='blue', linestyle='--', fill=False)
    ax.add_patch(water_pressure_triangle)

    # Add force arrows
    ax.arrow(base_breadth/2, height/2, 0, -weight * arrow_scale/4, head_width=head_width_scale, head_length=head_length_scale, fc='red', ec='red')
    ax.arrow(active_x_loc + active_soil_pressure * arrow_scale + head_length_scale, height / 3, -active_soil_pressure * arrow_scale, 0, head_width=head_width_scale, head_length=head_length_scale, fc='blue', ec='blue')
    ax.arrow(0 - passive_soil_pressure * arrow_scale - head_length_scale, passive_triangle_height / 3, passive_soil_pressure * arrow_scale, 0, head_width=head_width_scale, head_length=head_length_scale, fc='red', ec='red')
    ax.arrow(surcharge_x_loc + lateral_surcharge*arrow_scale + head_length_scale, height / 2, -lateral_surcharge * arrow_scale, 0, head_width=head_width_scale, head_length=head_length_scale, fc='blue', ec='blue')
    ax.arrow(water_x_loc + lateral_water * arrow_scale + head_length_scale, water_table / 3, -lateral_water * arrow_scale, 0, head_width=head_width_scale, head_length=head_length_scale, fc='blue', ec='blue')

    # Add force labels
    ax.text(base_breadth/2, height/2 - weight * arrow_scale/4 - head_length_scale, f"{weight:.2f} kN/m", color='red', fontsize=8, ha='center', va='center')
    ax.text(active_x_loc + active_soil_pressure * arrow_scale + head_length_scale, height / 3 + 0.1, f"{active_soil_pressure:.2f} kN/m", color='blue', fontsize=8, ha='center', va='center')
    ax.text(-2 * passive_soil_pressure * arrow_scale - head_length_scale, passive_triangle_height / 3, f"{passive_soil_pressure:.2f} kN/m", color='red', fontsize=8, ha='center', va='center')
    ax.text(surcharge_x_loc + lateral_surcharge * arrow_scale + head_length_scale, height/2 + 0.1, f"{lateral_surcharge:.2f} kN/m", color='blue', fontsize=8, ha='center', va='center')
    ax.text(water_x_loc + lateral_water * arrow_scale + head_length_scale, water_table/3 + 0.1, f"{lateral_water:.2f} kN/m", color='blue', fontsize=8, ha='center', va='center')

    x_max = water_x_loc + lateral_water * arrow_scale + head_length_scale + 1

    # Add active soil polygon
    soil_polygon = plt.Polygon([[base_breadth, 0], [top_breadth, height], [x_max, height], [x_max, 0]], closed=True, alpha=0.5, color='brown')
    ax.add_patch(soil_polygon)


    # Set plot limits and labels
    ax.set_xlim(-1* base_breadth, x_max)
    ax.set_ylim(0, 1.2 * height)
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")
    ax.set_title("Retaining Wall, Soil, and Forces")

    return fig






