def dist_between(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def point_inside_polygon(point, poly):
    """Determine if a point is inside a given polygon.
    point is a tuple of x, y. poly is a list of (x, y) tuples.
    Eg: point_inside_polygon((1, 2), [(0, 0), (10, 0), (0, 10)]) -> True
    http://www.ariel.com.au/a/python-point-int-poly.html
    
    """
    x, y = point
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def calc_work_x_y_yaw(base_x_map, base_y_map, target_x_map, target_y_map, working_dist):
    """Given the base position, a target object position, and the distance to
    be from the target to work on it,	computes the nearest position and yaw for
    the base which will put it at that working distance from the target.
    Assumes there are no obstacles.
    
    """
    # Variable name convention is: b = base, t = target, w = working position.
    # For example, wt_dx = the dx between the working position and target
    # position.
    b_x = base_x_map
    b_y = base_y_map
    t_x = target_x_map
    t_y = target_y_map
    wt_dist = working_dist
    
    # Find working position
    bt_dx = t_x - b_x
    bt_dy = t_y - b_y
    bt_dist = sqrt(bt_dx**2 + bt_dy**2)
    fraction = wt_dist / bt_dist
    wt_dx = fraction * bt_dx
    wt_dy = fraction * bt_dy
    w_x = t_x - wt_dx
    w_y = t_y - wt_dy
    
    # Find working yaw
    w_yaw = atan2(bt_dy, bt_dx)
    
    return w_x, w_y, w_yaw