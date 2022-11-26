def rgba2rgb( rgba, background=(255,255,255) ):
    row, col, ch = rgba.shape

    if ch == 3:
        return rgba

    assert ch == 4

    rgb = np.zeros( (row, col, 3), dtype='float32' )
    r, g, b, alpha = rgba[:,:,0], rgba[:,:,1], rgba[:,:,2], rgba[:,:,3]

    alpha = np.asarray( a, dtype='float32' ) / 255.0

    R, G, B = background

    rgb[:,:,0] = r * alpha + (1.0 - alpha) * R
    rgb[:,:,1] = g * alpha + (1.0 - alpha) * G
    rgb[:,:,2] = b * alpha + (1.0 - alpha) * B

    return np.asarray( rgb, dtype='uint8' )