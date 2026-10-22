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
Reisehaandbog over Norge: Reisehaandbog over Norge is a Norwegian travel guide book first published in 1879 by Yngvar Nielsen.  It was re-issued in twelve different editions between 1879 and 1915.  The guide book became quite popular, and played an important role in the development of tourism in Norway.  An English edition of the guide book was published in 1886.

Michelin Guide: Michelin Guides (French: "Guide Michelin" ] ) are a series of guide books published by the French tire company Michelin for more than a century.  The term normally refers to the annually published Michelin "Red Guide", the oldest European hotel and restaurant reference guide, which awards "Michelin stars" for excellence to a select few establishments.  The acquisition or loss of a star can have dramatic effects on the success of a restaurant.  Michelin also publishes a series of general guides to countries.

Christopher Kostow: Christopher Kostow (born 1976) is Executive Chef at The Restaurant at Meadowood in Napa Valley, California.  Under Chef Kostow, The Restaurant was awarded three stars from the Michelin Guide in 2011, 2012, 2013, 2014, 2015.  In 2013, Chef Kostow was awarded the James Beard Foundation Award for “Best Chef: West.”

Kono Mystery ga Sugoi!: Kono Mystery ga Sugoi!  (このミステリーがすごい!  , Kono Misuterī ga Sugoi!  , lit.  "This Mystery is Excellent!")  is an annual mystery fiction guide book published by Takarajimasha.  The guide book publishes a list of the top ten mystery books published in Japan in the previous year.

Enoteca Pinchiorri: Enoteca Pinchiorri is an Italian restaurant in Florence, Italy.  The owners are Giorgio Pinchiorri and French-born Annie Féolde.  The chefs are Annie Féolde, Italo Bassi and Riccardo Monco.  In 2008, the restaurant was voted 32nd best in the world by the British "Restaurant" magazine.  Since 1984, the restaurant has been a recipient of the "Wine Spectator" Grand Award.  It has perennially been awarded three stars by the Michelin Guide since 1993.

Helmut Thieltges: Helmut Thieltges (24 September 1955 – 26 July 2017) was a German chef.  Since 1978, he had been chef at the "Waldhotel Sonnora", his own family business.  Beginning in 1999, his restaurant was awarded three stars by the Michelin Guide for eighteen consecutive years.

Kono Light Novel ga Sugoi!: Kono Light Novel ga Sugoi!  (このライトノベルがすごい!  , Kono Raito Noberu ga Sugoi!  , lit.  "This Light Novel is Amazing!")  is an annual light novel guide book published by Takarajimasha.  The guide book publishes a list of the top ten most popular light novels and their characters according to readers polled on the Internet.  An introduction to each of the works comes with each listing, along with an interview of the light novel's author or authors for first place.  Many of the light novels that have been listed in this guide book were later adapted into anime series.  Most of the light novels listed contain a series of volumes, but some single-volume light novels also get listed.  The first release of the guide book was on November 26, 2004 and is the 2005 listing.  The latest release is the thirteenth volume on November 24, 2016 and is the 2017 listing. " Toaru Majutsu no Index" has appeared in the top ten in nine out of thirteen issues of "Kono Light Novel ga Sugoi!" , while "Sword Art Online" has appeared in seven, "Baka to Test to Shōkanjū" has appeared in six, and the "Haruhi Suzumiya" series and the "Book Girl" series have appeared in five.

A Guide Book of United States Coins: A Guide Book of United States Coins (Red Book), by Richard (R. S.) Yeoman, ISBN  , is a pricing guide for United States coin collectors, and is considered one of the most authoritative coin price sources.  The book is the longest running coin price guide.  The first edition, dated 1947, went on sale November 1946.  After the first three editions (dated 1947, 1948, 1949), the "Guide Book" was not published in 1949; annual publication resumed in 1950 with the 4th edition (dated 1951–1952) and has continued to this day.  The book's all-time peak print run for a single year was 1.2 million copies in 1965.  The 70th edition, cover-dated 2017, was published in 2016.

Honkaku Mystery Best 10: Honkaku Mystery Best 10 (本格ミステリ・ベスト10 , Honkaku Misuteri Besuto 10 ) is an annual mystery fiction guide book published by Hara Shobo.  The guide book publishes a list of the top ten honkaku (i.e. authentic, orthodox) mystery books published in Japan in the previous year.

Alinea (restaurant): Alinea is a restaurant in Chicago, Illinois, United States.  In 2010, Alinea was awarded three stars from the Michelin Guide, making it one of only two restaurants in Chicago with the award.

Question: the restaurant Alinea was awarded three stars from a guide book published every how many years ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "restaurant_name": {
      "type": "string",
      "description": "The name of the restaurant."
    },
    "guide_book_name": {
      "type": "string",
      "description": "The name of the guide book that awarded the stars."
    },
    "stars_awarded": {
      "type": "integer",
      "description": "The number of stars awarded to the restaurant."
    },
    "publication_frequency_years": {
      "type": "integer",
      "description": "The frequency, in years, at which the guide book is published."
    }
  },
  "required": [
    "restaurant_name",
    "guide_book_name",
    "stars_awarded",
    "publication_frequency_years"
  ],
  "additionalProperties": false
}
