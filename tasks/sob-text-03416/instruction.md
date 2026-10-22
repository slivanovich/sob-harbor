Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Willy Wonka &amp; the Chocolate Factory: Willy Wonka & the Chocolate Factory is a 1971 American musical fantasy film directed by Mel Stuart, and starring Gene Wilder as Willy Wonka.  It is an adaptation of the 1964 novel "Charlie and the Chocolate Factory" by Roald Dahl.  Dahl was credited with writing the film's screenplay; however, David Seltzer, who went uncredited in the film, was brought in to re-work Dahl's screenplay against his wishes, making major changes to the ending and adding musical numbers.  These changes and other decisions made by the director led Dahl to disown the film.

Wonka Bar: The Wonka Bar is both a fictional candy bar, introduced as a key story point in the 1964 novel "Charlie and the Chocolate Factory" by Roald Dahl, and a type of consumer product candy bar inspired by the fictional confection.  Wonka Bars appear in both film adaptations of the novel, "Willy Wonka & the Chocolate Factory" (1971) and "Charlie and the Chocolate Factory" (2005), and the play "Charlie and the Chocolate Factory the Musical" (2013) each with different packaging.

Spree (candy): Spree is a candy manufactured by The Willy Wonka Candy Company, a brand owned by Nestlé.  Spree was created by the Sunline Candy Company, later renamed Sunmark Corporation, of St. Louis, MO in the mid-1960s.  Spree was an idea of an employee named John Scout.  In the 1970s the brand was bought by Nestle' who markets the candy under the Willy Wonka brand.  Spree is classified as a compressed dextrose candy, covered in a colored fruit-flavored shell.  Depending on the market it is available in rolls or thin food type cardboard boxes.  A variation called Chewy Spree is also available in two distinct types: Chewy Spree Original and Chewy Spree Mixed Berry.  Chewy Spree boasts a similar size and shape as classic Spree, but with a chewy center.  Chewy Spree is available in pouches, rather than rolls.

Willy Wonka: Willy Wonka is a fictional character in Roald Dahl's 1964 children's novel "Charlie and the Chocolate Factory", its sequel "Charlie and the Great Glass Elevator", and the film adaptations of these books that followed.

The Scarecrow (2013 film): The Scarecrow is a 2013 animated short film and advertisement by the American restaurant chain Chipotle Mexican Grill.  The film features Fiona Apple singing a cover version of "Pure Imagination", originally performed by Gene Wilder as Willy Wonka in the 1971 film "Willy Wonka & the Chocolate Factory".

Pure Imagination: "Pure Imagination" is a song from the 1971 movie "Willy Wonka & the Chocolate Factory".  It was written by British composers Leslie Bricusse and Anthony Newley specifically for the movie.  It was sung by Gene Wilder (Willy Wonka).  The intro of the song, which also is the musical code for entering the Chocolate Room played by Willy Wonka, is the introduction of Wolfgang Amadeus Mozart's "Marriage of Figaro".

Roald Dahl's Willy Wonka (musical): Roald Dahl's Willy Wonka is a musical that combines elements of both Roald Dahl's book "Charlie and the Chocolate Factory" and of the 1971 movie "Willy Wonka & the Chocolate Factory" with newly created material.  The musical has several versions: the original version which premiered in 2004, the Junior version, the Kids version, and the Theatre for Young Audiences version.  All are owned by Music Theatre International, the company that owns the Willy Wonka license.

The Willy Wonka Candy Company: The Willy Wonka Candy Company is a British brand of confectionery owned and licensed by Swiss corporation Nestlé.  The Wonka brand's inception comes from materials licensed from British author Roald Dahl.  His classic children's novel, "Charlie and the Chocolate Factory", and its film adaptations are the source of both the packaging and the marketing styles of the Wonka brand.  The brand was launched in 1971, coinciding with the release of the novel's first film adaptation.  In 1988 the Willy Wonka Candy Company brand – then owned by Sunmark Corporation – was acquired by Nestlé.  Nestlé sells sweets and chocolate under the Willy Wonka brand name in the United States, Canada, the United Kingdom, the Republic of Ireland, Australia, New Zealand, Japan, South Africa, Mexico, Colombia, Brazil, Argentina, Costa Rica, Panama, Dominican Republic and the Middle East.  In mid-2015 the Willy Wonka brand name was dropped by Nestlé, in favour of special "throwback" packaging.  Candies previously made by the Willy Wonka brand are now under the Nestlé brand naming, excluding the Wonka brand name on the top left corner.

Wacky Wafers: Wacky Wafers were part of The Willy Wonka Candy Company line available in the United States.  They were shaped about the size of an American half dollar coin and came in five flavors: banana, green apple, watermelon, orange and strawberry.  Sold in a clear plastic wrapper, you could see the long strip of multi-colored and flavored wacky wafers inside.  Later, they were produced in a smaller version similar to the current bottle caps in a box filled with the miniature fruit-flavored snacks.  Wacky Wafers were discontinued as part of the regular product line when Nestlé purchased the Willy Wonka brand, but they may be reintroduced in 2012 by Leaf Brands, LLC.

Pure Imagination (album): Pure Imagination is a 1998 album by jazz pianist Eric Reed released through Impulse!  Records.  This album contains reinterpretations (remakes) of traditional pop songs from classic Broadway and Hollywood productions such as "Willy Wonka & the Chocolate Factory", "Porgy and Bess", "A Little Night Music" among others.  "Pure Imagination" has peaked at #8 on Billboard's Top Jazz Album charts.  All songs are written by famous songwriters of said productions except for the opening and closing tracks composed by Reed himself.

Question: "Pure Imagination" was a cover version sung by Fiano Apple which was oroginally performed by Gene Wilder as Willy Wonka from the adaptation of the children's novel which came out in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "original_performer": {
      "type": "string",
      "description": "The name of the artist who originally performed the song."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film where the song was originally featured."
    },
    "novel_title": {
      "type": "string",
      "description": "The title of the novel that the film was an adaptation of."
    },
    "novel_publication_year": {
      "type": "integer",
      "description": "The publication year of the children's novel."
    },
    "cover_performer": {
      "type": "string",
      "description": "The name of the artist who performed the cover version of the song."
    }
  },
  "required": [
    "song_title",
    "original_performer",
    "film_title",
    "novel_title",
    "novel_publication_year",
    "cover_performer"
  ],
  "additionalProperties": false
}
