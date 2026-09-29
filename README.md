# C09X – CSS Image Rollover

## Objective

Create a web page for the San Joaquin Valley Town Hall that demonstrates an
image rollover using CSS background images.

When the mouse is placed over the rollover area:

- The default image should display `sampson_dinosaur.jpg`.
- The image should change to `sorkin_desk260.jpg` when the user hovers over it.

## Requirements

### HTML

Your page must:

1. Use HTML5 document structure.
2. Set the page language to English.
3. Include the title:

   San Joaquin Valley Town Hall

4. Include a `<header>`.
5. Include the Town Hall logo.
6. Include the heading:

   San Joaquin Valley Town Hall

7. Include:

   Celebrating our 75th Year

8. Include a `<main>` element.
9. Include a `<section>` containing the rollover.
10. Include an `<aside>` containing the guest speakers.
11. Include a `<footer>`.
12. Include the guest speakers:
    - Jeffrey Toobin
    - Andrew Ross Sorkin
    - Amy Chua
    - Scott Sampson

### CSS

Your stylesheet must:

1. Reset margins and padding.
2. Set the body width to 850px.
3. Center the body.
4. Add a 3px solid `#931420` border.
5. Create the header styling.
6. Float the logo to the left.
7. Create the main section and aside layout.
8. Create the rollover using CSS background images.

The rollover must use:

```css
#image1 {
    background-image: url("../images/sampson_dinosaur.jpg");
    width: 260px;
    height: 260px;
    background-repeat: no-repeat;
}

#image1:hover {
    background-image: url("../images/sorkin_desk260.jpg");
}
