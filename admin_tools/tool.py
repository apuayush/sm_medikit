
class bst_cancer:

    def output():
        print "out"
        radius_mean_val = float(radius_mean.get())
        texture_mean_val = float(texture_mean.get())
        perimeter_mean_val = float(perimeter_mean.get())
        area_mean_val = float(area_mean.get())
        smoothness_mean_val = float(smoothness_mean.get())
        compactness_mean_val = float(compactness_mean.get())
        concavity_mean_val = float(concavity_mean.get())
        concave_val = float(concave.get())
        symmetry_mean_val = float(symmetry_mean.get())
        fractal_dimension_mean_val = float(fractal_dimension_mean.get())

    main = Tk()
    main.resizable(0, 0)
    fnt = (None, 20)

    Label(main, text="radius_mean", font=fnt).grid(row=0, column=0)
    Label(main, text="texture_mean", font=fnt).grid(row=1, column=0)
    Label(main, text="perimeter_mean", font=fnt).grid(row=2, column=0)
    Label(main, text="area_mean", font=fnt).grid(row=3, column=0)
    Label(main, text="smoothness_mean", font=fnt).grid(row=4, column=0)
    Label(main, text="compactness_mean", font=fnt).grid(row=5, column=0)
    Label(main, text="concavity_mean", font=fnt).grid(row=6, column=0)
    Label(main, text="concave points_mean", font=fnt).grid(row=7, column=0)
    Label(main, text="symmetry_mean", font=fnt).grid(row=8, column=0)
    Label(main, text="fractal_dimension_mean", font=fnt).grid(row=9, column=0)

    radius_mean = Entry(main, font=fnt)
    radius_mean.grid(row=0, column=1)
    texture_mean = Entry(main, font=fnt)
    texture_mean.grid(row=1, column=1)
    perimeter_mean = Entry(main, font=fnt)
    perimeter_mean.grid(row=2, column=1)
    area_mean = Entry(main, font=fnt)
    area_mean.grid(row=3, column=1)
    smoothness_mean = Entry(main, font=fnt)
    smoothness_mean.grid(row=4, column=1)
    compactness_mean = Entry(main, font=fnt)
    compactness_mean.grid(row=5, column=1)
    concavity_mean = Entry(main, font=fnt)
    concavity_mean.grid(row=6, column=1)
    concave = Entry(main, font=fnt)
    concave.grid(row=7, column=1)
    symmetry_mean = Entry(main, font=fnt)
    symmetry_mean.grid(row=8, column=1)
    fractal_dimension_mean = Entry(main, font=fnt)
    fractal_dimension_mean.grid(row=9, column=1)

    Button(main, text='Quit', bg='red', font=fnt, command=main.destroy).\
        grid(row=10, column=0, sticky=W, pady=4)
    Button(main, text='Output',bg='green', font=fnt, command=output).\
        grid(row=10, column=1, sticky=W, pady=4)
    mainloop()
