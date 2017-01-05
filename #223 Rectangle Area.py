#223 Rectangle Area

'''Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.'''

'''***S1+S2-Overlap***'''
def computeArea(A, B, C, D, E, F, G, H):
    S1 = (C-A)*(D-B)
    S2 = (G-E)*(H-F)
    S = S1+S2
    if C<=E or G<=A or D<=F or H<=B:
        return S
    else:
        xlap = min(C,G)-max(A,E)
        ylap = min(D,H)-max(B,F)
        S -= xlap*ylap
        return S
