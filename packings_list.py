# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr


packings_str = '''
    Raschig Super-Ring | metal   |   0.3    | 180000 | 315.0 | 0.960 | 3.560 | 2.340 | 0.750 | 0.760 | 1.500 | 0.450
    Raschig Super-Ring | metal   |   0.5    | 145000 | 250.0 | 0.975 | 3.350 | 2.200 | 0.620 | 0.780 | 1.450 | 0.430
    Raschig Super-Ring | metal   |   1.0    |  32000 | 160.0 | 0.980 | 3.491 | 2.200 | 0.750 | 0.500 | 1.290 | 0.440
    Raschig Super-Ring | metal   |   2.0    |   9500 |  97.6 | 0.985 | 3.326 | 2.096 | 0.720 | 0.464 | 1.323 | 0.400
    Raschig Super-Ring | metal   |   3.0    |   4300 |  80.0 | 0.982 | 3.260 | 2.100 | 0.620 | 0.430 | 0.850 | 0.300
    Raschig Super-Ring | plastic |   2.0    |   9000 | 100.0 | 0.960 | 3.326 | 2.096 | 0.720 | 0.377 | 1.250 | 0.337
    Ralu Flow          | plastic |   1.0    |  33000 | 165.0 | 0.940 | 3.612 | 2.401 | 0.640 | 0.485 | 1.486 | 0.360
    Ralu Flow          | plastic |   2.0    |   4600 | 100.0 | 0.945 | 3.412 | 2.174 | 0.640 | 0.350 | 1.270 | 0.320
    Pall ring          | metal   |  25.0    |  53900 | 223.5 | 0.954 | 2.627 | 2.083 | 0.719 | 0.957 | 1.440 | 0.336
    Pall ring          | metal   |  35.0    |  19517 | 139.4 | 0.965 | 2.629 | 1.679 | 0.644 | 0.967 | 1.012 | 0.341
    Pall ring          | metal   |  50.0    |   6242 | 112.6 | 0.951 | 2.725 | 1.580 | 0.784 | 0.763 | 1.192 | 0.410
    Pall ring          | plastic |  25.0    |  52300 | 225.0 | 0.887 | 2.696 | 2.064 | 0.528 | 0.865 | 0.905 | 0.446
    Pall ring          | plastic |  35.0    |  17000 | 151.1 | 0.906 | 2.654 | 1.742 | 0.718 | 0.927 | 0.856 | 0.380
    Pall ring          | plastic |  50.0    |   6765 | 111.1 | 0.919 | 2.816 | 1.757 | 0.593 | 0.698 | 1.239 | 0.368
    Pall ring          | ceramic |  50.0    |   7502 | 155.2 | 0.754 | 3.793 | 3.024 | 1.006 | 0.233 | 1.278 | 0.333
    Ralu ring          | metal   |  25.0    |  51000 | 215.0 | 0.960 | 2.627 | 2.083 | 0.714 | 0.957 | 1.440 | 0.336
    Ralu ring          | metal   |  38.0    |  14500 | 135.0 | 0.965 | 2.629 | 1.679 | 0.644 | 1.003 | 1.277 | 0.341
    Ralu ring          | metal   |  50.0    |   6300 | 105.0 | 0.975 | 2.725 | 1.580 | 0.784 | 0.763 | 1.192 | 0.345
    Ralu ring          | plastic |  25.0    |  36000 | 190.0 | 0.940 | 2.841 | 1.989 | 0.719 | 0.800 | 1.320 | 0.333
    Ralu ring          | plastic |  38.0    |  13500 | 150.0 | 0.930 | 2.843 | 1.812 | 0.640 | 0.672 | 1.320 | 0.333
    Ralu ring          | plastic |  50.0    |   5770 |  95.2 | 0.983 | 2.843 | 1.812 | 0.640 | 0.468 | 1.520 | 0.303
    NOR PAC ring       | plastic |  25.0    |  48920 | 197.9 | 0.920 | 2.865 | 2.083 | 0     | 0.383 | 0.976 | 0.410
    NOR PAC ring       | plastic |  25.0    |  50000 | 202.0 | 0.953 | 3.277 | 2.472 | 0.601 | 0.397 | 0.883 | 0.366
    NOR PAC ring       | plastic |  35.0    |  17450 | 141.8 | 0.944 | 3.179 | 2.242 | 0.587 | 0.371 | 0.756 | 0.425
    NOR PAC ring       | plastic |  50.0    |   7330 |  86.8 | 0.947 | 2.959 | 1.786 | 0.651 | 0.350 | 1.080 | 0.322
    Hiflow-ring        | metal   |  25.0    |  40790 | 202.9 | 0.962 | 2.918 | 2.177 | 0.799 | 0.689 | 1.641 | 0.402
    Hiflow-ring        | metal   |  50.0    |   6815 | 117.1 | 0.925 | 2.894 | 1.871 | 1.038 | 0.327 | 1.478 | 0.345
    Hiflow-ring        | metal   |  50.0    |   5000 |  92.3 | 0.977 | 2.702 | 1.626 | 0.876 | 0.421 | 1.168 | 0.408
    Hiflow-ring        | plastic |  25.0    |  46100 | 194.5 | 0.918 | 2.841 | 1.989 | 0     | 0.741 | 1.577 | 0.390
    Hiflow-ring        | plastic |  50S     |   6050 |  82.0 | 0.942 | 2.866 | 1.702 | 0.881 | 0.414 | 1.219 | 0.342
    Hiflow-ring        | plastic |  50hydr  |   6890 | 118.4 | 0.925 | 2.894 | 1.871 | 0     | 0.311 | 1.553 | 0.369
    Hiflow-ring        | ceramic |  20.0    | 121314 | 286.2 | 0.758 | 2.875 | 2.410 | 1.167 | 0.628 | 1.744 | 0.465
    Hiflow-ring        | ceramic |  38.0    |  13241 | 111.8 | 0.788 | 2.840 | 1.930 | 0     | 0.621 | 1.659 | 0.464
    Hiflow-ring        | ceramic |  50.0    |   5120 |  89.7 | 0.809 | 2.819 | 1.694 | 0     | 0.538 | 1.377 | 0.379
    Glitsch Ring       | metal   |  30PMK   |  29200 | 180.5 | 0.975 | 2.694 | 1.900 | 0.930 | 0.851 | 1.920 | 0.450
    Glitsch Ring       | metal   |  30P     |  31100 | 164.0 | 0.959 | 2.564 | 1.760 | 0.851 | 1.056 | 1.577 | 0.398
    Glitsch CMR ring   | metal   |   0.5"   | 560811 | 356.0 | 0.952 | 2.644 | 2.178 | 0     | 0.882 | 2.038 | 0.495
    Glitsch CMR ring   | metal   |   1.0"   | 158467 | 232.5 | 0.971 | 2.703 | 1.996 | 1.040 | 0.641 | 0     | 0
    Glitsch CMR ring   | metal   |   1.5"T  |  63547 | 188.0 | 0.972 | 2.790 | 1.870 | 0.870 | 0.627 | 0     | 0
    Glitsch CMR ring   | metal   |   1.5"   |  60744 | 174.9 | 0.974 | 2.697 | 1.841 | 0.935 | 0.632 | 0     | 0
    TOP Pak ring       | alu     |  50.0    |   6871 | 105.5 | 0.956 | 2.528 | 1.579 | 0.881 | 0.604 | 1.326 | 0.389
    Raschig ring       | ceramic |  25.0    |  47700 | 190.0 | 0.680 | 2.454 | 1.899 | 0.577 | 1.329 | 1.361 | 0.412
    Raschig ring       | ceramic |  50.0    |   5990 |  95.0 | 0.830 | 2.482 | 1.547 | 0     | 0     | 1.416 | 0.210
    VSP ring           | metal   |  25.0    |  33434 | 199.6 | 0.975 | 2.755 | 1.970 | 1.369 | 0.782 | 1.376 | 0.405
    VSP ring           | metal   |  50.0    |   7841 | 104.6 | 0.980 | 2.806 | 1.689 | 1.135 | 0.773 | 1.222 | 0.420
    Envi Pac ring      | plastic |  32.0    |  53000 | 138.9 | 0.936 | 2.944 | 2.012 | 1.039 | 0.549 | 1.517 | 0.459
    Envi Pac ring      | plastic |  60.0    |   6800 |  98.4 | 0.961 | 2.987 | 1.864 | 0.794 | 0.338 | 1.522 | 0.296
    Envi Pac ring      | plastic |  80.0    |   2000 |  60.0 | 0.955 | 2.846 | 1.522 | 0.641 | 0.358 | 1.603 | 0.257
    Bialecki ring      | metal   |  25.0    |  48533 | 210.0 | 0.956 | 2.521 | 1.856 | 0.692 | 0.891 | 1.461 | 0.331
    Bialecki ring      | metal   |  35.0    |  18200 | 155.0 | 0.967 | 2.753 | 1.885 | 0.787 | 1.011 | 1.412 | 0.390
    Bialecki ring      | metal   |  35.0    |  20736 | 176.6 | 0.945 | 0     | 0     | 0.690 | 0.460 | 1.405 | 0.377
    Bialecki ring      | metal   |  50.0    |   6278 | 121.0 | 0.966 | 2.916 | 1.896 | 0.798 | 0.719 | 1.721 | 0.302
    Tellerette         | plastic |  25.0    |  37037 | 190.0 | 0.930 | 2.913 | 2.132 | 0.588 | 0.538 | 0.899 | 0
    Hackette           | plastic |  45.0    |  12000 | 139.5 | 0.928 | 2.832 | 1.966 | 0.643 | 0.399 | 0     | 0
    Raflux ring        | plastic |  15.0    | 193522 | 307.9 | 0.894 | 2.825 | 2.400 | 0.491 | 0.595 | 1.913 | 0.370
    Berl saddle        | ceramic |  13.0    | 691505 | 545.0 | 0.650 | 0     | 0     | 0.833 | 0     | 1.364 | 0.232
    Berl saddle        | ceramic |  25.0    |  80080 | 260.0 | 0.680 | 0     | 0     | 0.620 | 0     | 1.246 | 0.387
    DIN-PAK            | plastic |  47.0    |  28168 | 131.2 | 0.923 | 2.929 | 1.991 | 1.173 | 0.514 | 1.690 | 0.354
    DIN-PAK            | plastic |  70.0    |   9763 | 110.7 | 0.938 | 2.970 | 1.912 | 0.991 | 0.378 | 1.527 | 0.326
    Ralu pak           | metal   | YC-250   |      0 | 250.0 | 0.945 | 3.178 | 2.558 | 0     | 0.191 | 1.334 | 0.385
    Mellapak           | metal   | 250Y     |      0 | 250.0 | 0.970 | 3.157 | 2.464 | 0.554 | 0.292 | 0     | 0
    Gempack            | metal   | A2T-304  |      0 | 202.0 | 0.977 | 2.986 | 2.099 | 0.678 | 0.344 | 0     | 0
    Impulse packing    | metal   | 250.0    |      0 | 250.0 | 0.975 | 2.610 | 1.996 | 0.431 | 0.262 | 0.983 | 0.270
    Impulse packing    | ceramic | 100.0    |      0 |  91.4 | 0.838 | 2.664 | 1.655 | 1.900 | 0.417 | 1.317 | 0.327
    Montz packing      | metal   | B1-200   |      0 | 200.0 | 0.979 | 3.116 | 2.339 | 0.547 | 0.355 | 0.971 | 0.390
    Montz packing      | metal   | B2-300   |      0 | 300.0 | 0.930 | 3.098 | 2.464 | 0.482 | 0.295 | 1.165 | 0.422
    Montz packing      | plastic | C1-200   |      0 | 200.0 | 0.954 | 0     | 0     | 0     | 0.453 | 1.006 | 0.412
    Montz packing      | plastic | C2-200   |      0 | 200.0 | 0.900 | 2.653 | 1.973 | 0     | 0.481 | 0.739 | 0
    Euroform           | plastic | PN-110   |      0 | 110.0 | 0.936 | 3.075 | 1.975 | 0.511 | 0.250 | 0.973 | 0.167
'''



packings = []

for line in packings_str.strip().splitlines():
    line_items = line.split(" | ")
    line_items = [s.strip() for s in line_items]
    name, material, size, N, a, eps, CS, CFl, Ch, CP0, CL, CV = line_items
    packings.append({
        'name': name,
        'material': material,
        'size': size,
        'N': int(N),
        'a': float(a),
        'eps': float(eps),
        'CS': float(CS),
        'CFl': float(CFl),
        'Ch': float(Ch),
        'CP0': float(CP0),
        'CL': float(CL),
        'CV': float(CV),
    })



# EXPORTING PACKING NAME
seen_packing_name = set()
export_packing_name = []

for i in range(len(packings)):
    if packings[i]["name"] not in seen_packing_name:
        seen_packing_name.add(packings[i]["name"])        
        export_packing_name.append(packings[i]["name"])
    else:
        pass


# EXPORT PACKING SURFACEAREA
export_packing_surfacearea = []

for item in packings:
    if item["name"] == type_packing:
        export_packing_surfacearea.append(item["a"])

print(export_packing_surfacearea)
