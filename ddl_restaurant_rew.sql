
CREATE TABLE IF NOT EXISTS restaurants_reviews(
    gmap_id text,
    name text,
    rating integer,
    reviews text,
    user_id text,
    "date" text
);

CREATE TABLE IF NOT EXISTS misc_categories(
    gmap_id text,
    Accessibility text[],
    Activities text[],
    Amenities text[],
    Atmosphere text[],
    Crowd text[],
    Dining_options text[],
    From_the_business text[],
    Getting_here text[],
    Health_and_safety text[],
    Health_and_safety_1 text[],
    Highlights text[],
    Lodging_options text[],
    Offerings text[],
    Payments text[],
    Planning text[],
    Popular_for text[],
    Recycling text[],
    Service_options text[]
    
);

DROP TABLE misc_categories;