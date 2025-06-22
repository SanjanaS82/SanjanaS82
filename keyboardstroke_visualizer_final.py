import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from collections import deque
import math

#homepagecreation
class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Navigation Visualizer")
        self.root.geometry("1200x800")
        self.root.configure(bg="#C10B66")
        
        # Center the window
        self.center_window()
        
        self.create_home_page()
    
    def center_window(self):
        self.root.update_idletasks()  # Update "requested size" from geometry manager
        x = (self.root.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.root.winfo_screenheight() // 2) - (800 // 2)
        self.root.geometry(f"1200x800+{x}+{y}")
    
    def create_home_page(self):
        # Main container
        main_frame = tk.Frame(self.root, bg="#C10B66")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add some vertical spacing
        tk.Frame(main_frame, bg="#C10B66", height=80).pack()
        
        # Title section
        title_frame = tk.Frame(main_frame, bg="#C10B66")
        title_frame.pack(pady=30)
        
        # Main title
        title_label = tk.Label(title_frame, 
                              text="Keyboard Navigation Visualizer", 
                              font=("Arial", 36, "bold"), 
                              fg="white", 
                              bg="#C10B66")
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(title_frame, 
                                 text="Find the optimal path for typing on custom keyboard layouts", 
                                 font=("Arial", 16), 
                                 fg="#FFE6F0", 
                                 bg="#C10B66")
        subtitle_label.pack(pady=(10, 0))
        
        # Features section
        features_frame = tk.Frame(main_frame, bg="#C10B66")
        features_frame.pack(pady=50)
        
        features_title = tk.Label(features_frame, 
                                 text="Features", 
                                 font=("Arial", 24, "bold"), 
                                 fg="white", 
                                 bg="#C10B66")
        features_title.pack(pady=(0, 20))
        
        # Feature list
        features = [
            "🔲 Create custom keyboard grid layouts",
            "🎯 Calculate optimal navigation paths",
            "📊 Visualize movement with interactive graphics",
            "📈 Get detailed stroke count analysis",
            "⚡ Find shortest paths using advanced algorithms"
        ]
        
        for feature in features:
            feature_label = tk.Label(features_frame, 
                                   text=feature, 
                                   font=("Arial", 14), 
                                   fg="#FFE6F0", 
                                   bg="#C10B66",
                                   anchor="w")
            feature_label.pack(pady=8)
        
        # Start button section
        button_frame = tk.Frame(main_frame, bg="#C10B66")
        button_frame.pack(pady=60)
        
        # Stylish start button
        start_button = tk.Button(button_frame,
                               text="Start Application",
                               font=("Arial", 18, "bold"),
                               fg="white",
                               bg="#4F034F",
                               activebackground="#7A0B7A",
                               activeforeground="white",
                               relief="raised",
                               bd=3,
                               padx=40,
                               pady=15,
                               cursor="hand2",
                               command=self.start_application)
        start_button.pack()
        
        # Add hover effects
        def on_enter(e):
            start_button.config(bg="#7A0B7A", relief="raised", bd=4)
        
        def on_leave(e):
            start_button.config(bg="#4F034F", relief="raised", bd=3)
        
        start_button.bind("<Enter>", on_enter)
        start_button.bind("<Leave>", on_leave)
        
        # Footer
        footer_frame = tk.Frame(main_frame, bg="#C10B66")
        footer_frame.pack(side=tk.BOTTOM, pady=20)
        
        footer_label = tk.Label(footer_frame, 
                               text="Optimize your typing efficiency with intelligent path finding", 
                               font=("Arial", 12, "italic"), 
                               fg="#D37DA8", 
                               bg="#C10B66")
        footer_label.pack()
    
    def start_application(self):
        # Hide the home page
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Start the main application
        app = KeyboardVisualizerGUI(self.root)

class KeyboardVisualizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Navigation Visualizer - Main Application")
        self.root.geometry("1600x1000")  # Increased from 1200x800
        self.root.configure(bg="#C10B66")
        
        # Variables
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.char_map = {}
        self.canvas = None
        self.cell_size = 80  # Increased from 60
        self.path_history = []
        
        self.setup_ui()
        
        # Add back button
        self.add_back_button()
    
    def add_back_button(self):
        # Add a back to home button in the top-left corner
        back_frame = tk.Frame(self.root, bg="#C10B66")
        back_frame.place(x=10, y=10)
        
        back_button = tk.Button(back_frame,
                               text="← Home",
                               font=("Arial", 12, "bold"),
                               fg="white",
                               bg="#4F034F",
                               activebackground="#7A0B7A",
                               activeforeground="white",
                               relief="raised",
                               bd=2,
                               padx=15,
                               pady=5,
                               cursor="hand2",
                               command=self.go_home)
        back_button.pack()
        
        # Add hover effects
        def on_enter(e):
            back_button.config(bg="#7A0B7A")
        
        def on_leave(e):
            back_button.config(bg="#4F034F")
        
        back_button.bind("<Enter>", on_enter)
        back_button.bind("<Leave>", on_leave)
    
    def go_home(self):
        # Destroy current application
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Return to home page
        home = HomePage(self.root)
    
    def setup_ui(self):
        # Main frame with larger padding - adjusted for back button
        main_frame = ttk.Frame(self.root, padding="15")  # Increased from 10
        main_frame.configure(style="Pink.TFrame")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 0), pady=(50, 0))  # Added top padding for back button
        
        # Configure pink style
        style = ttk.Style()
        style.configure("Pink.TFrame", background="#D37DA8")
        style.configure("Pink.TLabelframe", background="#D37DA8")
        style.configure("Pink.TLabelframe.Label", background="#D37DA8", font=("Arial", 12, "bold"))  # Larger font
        
        # Input frame with larger padding
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding="15", style="Pink.TLabelframe")  # Increased from 10
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 15))  # Increased from 10
        
        # Grid size inputs with larger fonts and entries
        ttk.Label(input_frame, text="Rows:", font=("Arial", 11)).grid(row=0, column=0, padx=(0, 8))  # Larger font and padding
        self.rows_var = tk.StringVar()
        rows_entry = ttk.Entry(input_frame, textvariable=self.rows_var, width=12, font=("Arial", 11))  # Larger width and font
        rows_entry.grid(row=0, column=1, padx=(0, 15))
        
        ttk.Label(input_frame, text="Cols:", font=("Arial", 11)).grid(row=0, column=2, padx=(0, 8))
        self.cols_var = tk.StringVar()
        cols_entry = ttk.Entry(input_frame, textvariable=self.cols_var, width=12, font=("Arial", 11))
        cols_entry.grid(row=0, column=3, padx=(0, 15))
        
        create_btn = ttk.Button(input_frame, text="Create Grid", command=self.create_grid_input)
        create_btn.configure(style="Large.TButton")
        create_btn.grid(row=0, column=4, padx=(15, 0))
        
        # Configure larger button style
        style.configure("Large.TButton", font=("Arial", 11), padding=(10, 5))
        
        # Text input with larger elements
        ttk.Label(input_frame, text="Text to type:", font=("Arial", 11)).grid(row=1, column=0, padx=(0, 8), pady=(15, 0))  # Increased padding
        self.text_var = tk.StringVar()
        text_entry = ttk.Entry(input_frame, textvariable=self.text_var, width=40, font=("Arial", 11))  # Larger width and font
        text_entry.grid(row=1, column=1, columnspan=3, sticky=(tk.W, tk.E), pady=(15, 0))
        
        calc_btn = ttk.Button(input_frame, text="Calculate Path", command=self.calculate_and_visualize)
        calc_btn.configure(style="Large.TButton")
        calc_btn.grid(row=1, column=4, padx=(15, 0), pady=(15, 0))
        
        # Canvas frame with larger padding
        canvas_frame = ttk.LabelFrame(main_frame, text="Keyboard Visualization", padding="15", style="Pink.TLabelframe")
        canvas_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        
        # Canvas with scrollbars
        self.setup_canvas(canvas_frame)
        
        # Results frame with larger padding
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="15", style="Pink.TLabelframe")
        results_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))
        
        # Text widget with larger font and dimensions
        self.result_text = tk.Text(results_frame, height=10, width=100, font=("Arial", 11))  # Increased size and font
        scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        canvas_frame.columnconfigure(0, weight=1)
        canvas_frame.rowconfigure(0, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
    
    def setup_canvas(self, parent):
        # Create canvas with scrollbars
        canvas_container = ttk.Frame(parent)
        canvas_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.canvas = tk.Canvas(canvas_container, bg="#D37DA8", width=1000, height=500)  # Increased from 800x400
        h_scrollbar = ttk.Scrollbar(canvas_container, orient="horizontal", command=self.canvas.xview)
        v_scrollbar = ttk.Scrollbar(canvas_container, orient="vertical", command=self.canvas.yview)
        
        self.canvas.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
        
        self.canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        canvas_container.columnconfigure(0, weight=1)
        canvas_container.rowconfigure(0, weight=1)
    
    def create_grid_input(self):
        try:
            self.rows = int(self.rows_var.get())
            self.cols = int(self.cols_var.get())
            
            if self.rows <= 0 or self.cols <= 0:
                messagebox.showerror("Error", "Rows and columns must be positive integers.")
                return
            
            self.grid = []
            for r in range(self.rows):
                row = []
                for c in range(self.cols):
                    # Create a custom dialog with larger font
                    dialog = tk.Toplevel(self.root)
                    dialog.title("Grid Input")
                    dialog.geometry("400x200")  # Larger dialog
                    dialog.configure(bg="#D37DA8")
                    dialog.transient(self.root)
                    dialog.grab_set()
                    
                    # Center the dialog
                    dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
                    
                    # Add label with larger font
                    label = tk.Label(dialog, text=f"Enter character for position ({r},{c}):", 
                                   font=("Arial", 12), bg="#D37DA8", fg="black")
                    label.pack(pady=20)
                    
                    # Add entry with larger font
                    entry_var = tk.StringVar()
                    entry = tk.Entry(dialog, textvariable=entry_var, font=("Arial", 14), width=20)
                    entry.pack(pady=10)
                    entry.focus()
                    
                    # Add buttons with larger font
                    button_frame = tk.Frame(dialog, bg="#D37DA8")
                    button_frame.pack(pady=20)
                    
                    result = [None]  # Use list to store result
                    
                    def ok_clicked():
                        result[0] = entry_var.get().strip()
                        dialog.destroy()
                    
                    def cancel_clicked():
                        result[0] = None
                        dialog.destroy()
                    
                    ok_btn = tk.Button(button_frame, text="OK", command=ok_clicked, 
                                     font=("Arial", 11), width=10)
                    ok_btn.pack(side=tk.LEFT, padx=10)
                    
                    cancel_btn = tk.Button(button_frame, text="Cancel", command=cancel_clicked, 
                                         font=("Arial", 11), width=10)
                    cancel_btn.pack(side=tk.LEFT, padx=10)
                    
                    # Bind Enter key to OK
                    entry.bind('<Return>', lambda e: ok_clicked())
                    
                    dialog.wait_window()
                    
                    char = result[0]
                    if char is None:  # User cancelled
                        return
                    row.append(char)
                self.grid.append(row)
            
            self.char_map = self.create_char_position_map(self.grid)
            self.draw_keyboard()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for rows and columns.")
    
    def create_char_position_map(self, grid):
        char_map = {}
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                char = grid[r][c]
                if char not in char_map:
                    char_map[char] = []
                char_map[char].append((r, c))
        return char_map
    
    def draw_keyboard(self):
        self.canvas.delete("all")
        
        if not self.grid:
            return
        
        # Calculate canvas size with larger margins
        canvas_width = self.cols * self.cell_size + 150  # Increased margin from 100
        canvas_height = self.rows * self.cell_size + 150
        self.canvas.configure(scrollregion=(0, 0, canvas_width, canvas_height))
        
        # Draw grid with larger margins
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * self.cell_size + 75  # Increased margin from 50
                y1 = r * self.cell_size + 75
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                # Draw cell with thicker border
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="#4F034F", width=3)  # Increased width from 2
                
                # Draw character with larger font
                char = self.grid[r][c]
                self.canvas.create_text(x1 + self.cell_size//2, y1 + self.cell_size//2, 
                                      text=char, font=("Arial", 18, "bold"), fill="white")  # Increased from 14
    
    def get_next_different_key_coords(self, current_r, current_c, direction):
        current_key_char = self.grid[current_r][current_c]
        
        if direction == 'up':
            for r_check in range(current_r - 1, -1, -1):
                if self.grid[r_check][current_c] != current_key_char:
                    return (r_check, current_c)
        elif direction == 'down':
            for r_check in range(current_r + 1, self.rows):
                if self.grid[r_check][current_c] != current_key_char:
                    return (r_check, current_c)
        elif direction == 'left':
            for c_check in range(current_c - 1, -1, -1):
                if self.grid[current_r][c_check] != current_key_char:
                    return (current_r, c_check)
        elif direction == 'right':
            for c_check in range(current_c + 1, self.cols):
                if self.grid[current_r][c_check] != current_key_char:
                    return (current_r, c_check)
        
        return None
    
    def bfs_shortest_path_with_jumps(self, start_coords, target_char):
        """BFS to find shortest path with jump movements"""
        q = deque([(start_coords[0], start_coords[1], 0, [start_coords])])
        visited = set([start_coords])
        
        if self.grid[start_coords[0]][start_coords[1]] == target_char:
            return 0, start_coords, [start_coords]
        
        directions = ['up', 'down', 'left', 'right']
        
        while q:
            curr_r, curr_c, jumps, path = q.popleft()
            
            for direction in directions:
                next_coords = self.get_next_different_key_coords(curr_r, curr_c, direction)
                
                if next_coords and next_coords not in visited:
                    next_r, next_c = next_coords
                    visited.add(next_coords)
                    new_path = path + [next_coords]
                    
                    if self.grid[next_r][next_c] == target_char:
                        return jumps + 1, next_coords, new_path
                    
                    q.append((next_r, next_c, jumps + 1, new_path))
        
        return float('inf'), None, []
    
    def calculate_and_visualize(self):
        if not self.grid:
            messagebox.showerror("Error", "Please create a grid first.")
            return
        
        text_to_type = self.text_var.get().strip()
        if not text_to_type:
            messagebox.showerror("Error", "Please enter text to type.")
            return
        
        # Clear previous results
        self.result_text.delete(1.0, tk.END)
        self.path_history = []
        
        # Calculate path
        total_strokes = 0
        current_pos = (0, 0)
        enter_key_char = '*'
        
        # Check if enter key exists
        if enter_key_char not in self.char_map:
            messagebox.showerror("Error", f"Enter key '{enter_key_char}' not found in grid.")
            return
        
        full_sequence = text_to_type + enter_key_char
        detailed_results = []
        
        for i, target_char in enumerate(full_sequence):
            if target_char not in self.char_map:
                messagebox.showerror("Error", f"Character '{target_char}' not found in grid.")
                return
            
            jumps, reached_coords, path = self.bfs_shortest_path_with_jumps(current_pos, target_char)
            
            if jumps == float('inf'):
                messagebox.showerror("Error", f"Character '{target_char}' unreachable from {current_pos}.")
                return
            
            strokes = jumps + 1
            total_strokes += strokes
            
            # Store path for visualization
            self.path_history.append({
                'char': target_char,
                'path': path,
                'strokes': strokes,
                'from': current_pos,
                'to': reached_coords
            })
            
            detailed_results.append(f"'{target_char}': {jumps} moves + 1 select = {strokes} strokes")
            current_pos = reached_coords
        
        # Display results
        self.result_text.insert(tk.END, f"Text to type: '{text_to_type}'\n")
        self.result_text.insert(tk.END, f"Total minimum strokes: {total_strokes}\n\n")
        self.result_text.insert(tk.END, "Detailed breakdown:\n")
        for result in detailed_results:
            self.result_text.insert(tk.END, result + "\n")
        
        # Visualize path
        self.visualize_path()
    
    def visualize_path(self):
        # Redraw keyboard
        self.draw_keyboard()
        
        if not self.path_history:
            return
        
        # Draw all paths
        for i, path_info in enumerate(self.path_history):
            color = 'red'  # All arrows are red now
            path = path_info['path']
            
            # Draw path arrows
            for j in range(len(path) - 1):
                start_pos = path[j]
                end_pos = path[j + 1]
                
                self.draw_arrow(start_pos, end_pos, color)
            
            # Highlight start position with larger circles
            start_r, start_c = path[0]
            x = start_c * self.cell_size + 75 + self.cell_size//2  # Updated margin
            y = start_r * self.cell_size + 75 + self.cell_size//2
            self.canvas.create_oval(x-12, y-12, x+12, y+12, fill="#03009E", outline='black', width=3)  # Larger circles and thicker border
            
            # Highlight end position with larger circles
            if len(path) > 1:
                end_r, end_c = path[-1]
                x = end_c * self.cell_size + 75 + self.cell_size//2
                y = end_r * self.cell_size + 75 + self.cell_size//2
                self.canvas.create_oval(x-12, y-12, x+12, y+12, fill="#03009E", outline='black', width=3)
    
    def draw_arrow(self, start_pos, end_pos, color):
        start_r, start_c = start_pos
        end_r, end_c = end_pos
        
        # Calculate center points with updated margins
        start_x = start_c * self.cell_size + 75 + self.cell_size//2  # Updated margin from 50
        start_y = start_r * self.cell_size + 75 + self.cell_size//2
        end_x = end_c * self.cell_size + 75 + self.cell_size//2
        end_y = end_r * self.cell_size + 75 + self.cell_size//2
        
        # Draw arrow line with larger arrow
        self.canvas.create_line(start_x, start_y, end_x, end_y, 
                               fill=color, width=4, arrow=tk.LAST, arrowshape=(14, 16, 4))  # Larger arrow and thicker line

# Original algorithm functions (keeping the existing logic)
def create_grid(rows, cols):
    grid = []
    print(f"\nPlease enter {rows * cols} elements for your {rows}x{cols} keyboard grid:")
    for r in range(rows):
        row_elements = []
        for c in range(cols):
            element = input(f"Enter element for ({r},{c}): ").strip()
            row_elements.append(element)
        grid.append(row_elements)
    return grid

def create_char_position_map(grid):
    char_map = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            char = grid[r][c]
            if char not in char_map:
                char_map[char] = []
            char_map[char].append((r, c))
    return char_map

def get_next_different_key_coords(current_r, current_c, grid, max_rows, max_cols, direction):
    current_key_char = grid[current_r][current_c]
    
    if direction == 'up':
        for r_check in range(current_r - 1, -1, -1):
            if grid[r_check][current_c] != current_key_char:
                return (r_check, current_c)
    elif direction == 'down':
        for r_check in range(current_r + 1, max_rows):
            if grid[r_check][current_c] != current_key_char:
                return (r_check, current_c)
    elif direction == 'left':
        for c_check in range(current_c - 1, -1, -1):
            if grid[current_r][c_check] != current_key_char:
                return (current_r, c_check)
    elif direction == 'right':
        for c_check in range(current_c + 1, max_cols):
            if grid[current_r][c_check] != current_key_char:
                return (current_r, c_check)
    
    return None

def bfs_shortest_path_with_jumps(start_coords, target_char, grid, char_map, max_rows, max_cols):
    q = deque([(start_coords[0], start_coords[1], 0)])
    visited = set([start_coords])

    if grid[start_coords[0]][start_coords[1]] == target_char:
        return 0, start_coords

    directions = ['up', 'down', 'left', 'right']

    while q:
        curr_r, curr_c, jumps = q.popleft()

        for direction in directions:
            next_coords = get_next_different_key_coords(curr_r, curr_c, grid, max_rows, max_cols, direction)
            
            if next_coords:
                next_r, next_c = next_coords
                
                if next_coords not in visited:
                    visited.add(next_coords)
                    
                    if grid[next_r][next_c] == target_char:
                        return jumps + 1, next_coords

                    q.append((next_r, next_c, jumps + 1))
    
    return float('inf'), None

def calculate_total_strokes(text_to_type, keyboard_grid, char_map, grid_rows, grid_cols,
                            start_position=(0, 0), enter_key_char='*'):
    total_strokes = 0
    current_row, current_col = start_position

    if enter_key_char not in char_map:
        print(f"Error: The '{enter_key_char}' enter key was not found on the keyboard grid.")
        return -1

    full_typing_sequence = text_to_type + enter_key_char

    for i, target_char in enumerate(full_typing_sequence):
        if target_char not in char_map:
            print(f"Error: Character '{target_char}' from the text was not found on the keyboard.")
            return -1

        movement_jumps, reached_coords = bfs_shortest_path_with_jumps(
            (current_row, current_col),
            target_char,
            keyboard_grid,
            char_map,
            grid_rows,
            grid_cols
        )

        if movement_jumps == float('inf'):
            print(f"Error: Character '{target_char}' is unreachable from ({current_row},{current_col}).")
            return -1

        strokes_for_char = movement_jumps + 1
        total_strokes += strokes_for_char
        current_row, current_col = reached_coords

    return total_strokes

# Main execution
if __name__ == "__main__":
    choice = input("Choose interface: (1) GUI or (2) Console [default: 1]: ").strip()
    
    if choice == '2':
        # Original console version
        try:
            rows_input = int(input("Enter number of rows for the keyboard grid: "))
            cols_input = int(input("Enter number of columns for the keyboard grid: "))

            if rows_input <= 0 or cols_input <= 0:
                print("Rows and columns must be positive integers.")
                exit()

            keyboard_grid = create_grid(rows_input, cols_input)
            keyboard_layout_map = create_char_position_map(keyboard_grid)
            word_to_type = input("\nEnter the string to type: ")
            initial_cursor_position = (0, 0)
            enter_key_char = '*'

            final_strokes_count = calculate_total_strokes(
                word_to_type,
                keyboard_grid,
                keyboard_layout_map,
                rows_input,
                cols_input,
                start_position=initial_cursor_position,
                enter_key_char=enter_key_char
            )

            if final_strokes_count != -1:
                print(f"\nTotal minimal strokes: {final_strokes_count}")
            else:
                print("\nCalculation failed. Please check your input and keyboard layout.")

        except ValueError:
            print("Invalid input. Please enter integers for rows and columns.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        # GUI version with home page
        root = tk.Tk()
        home = HomePage(root)
        root.mainloop()
