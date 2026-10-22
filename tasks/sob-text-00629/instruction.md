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
Nigel Beauty Emporium: Nigel Beauty Emporium is a professional beauty supply store located in the NoHo Arts District of North Hollywood, California.  Since opening in 2007, it has become well known as a store "where Hollywood makeup artists go to keep the likes of Sandra Bullock, Megan Fox and George Clooney powdered and buffed".  Nigel Beauty Emporium carries a variety of professional cosmetics, skincare, haircare, special FX, tools, and accessories.

Spe Salvi: Spe Salvi (English: "Saved in Hope" ), referencing the Latin phrase from Romans , "Spe salvi facti sumus" ("in hope we were saved"), is the second encyclical letter by Pope Benedict XVI promulgated on November 30, 2007, and is about the theological virtue of hope.  Benedict has systematically touched upon the three theological virtues: love in 2005 "Deus caritas est" ("God is Love"), hope in this encyclical, and faith in 2013 "Lumen fidei" ("The Light of Faith"), written with Pope Francis.

Nalli (wardrobe store): Nalli is an Indian wardrobe store and silk saree emporium based in Chennai.  It is one of the oldest saree shops in the Chennai's commercial neighbourhood of T. Nagar.

Hope &amp; Faith: Hope & Faith is an American television sitcom, starring Faith Ford and Kelly Ripa as Hope Shanowski and Faith Fairfield.  Hope is a homemaker and mother of three and Faith is her sister, a soap opera star whose character is killed off, leading her to move in with Hope and her family in the fictional town of Glen Falls, Ohio.  It originally aired on ABC from September 26, 2003 to May 2, 2006.  During its first and second seasons, the series was part of the revived TGIF comedy block.

Sweatshop (retailer): Sweatshop is a chain of running equipment shops in the United Kingdom with 14 branches (as of September 2017) and an online shop.  It was founded by runner Chris Brasher in 1971, with the first shop in Teddington.  Its original name was Chris Brasher's Sporting Emporium, and changed to Sweatshop in 1978.  In 2014 Sports Direct became a major share holder.

Brewers Quay: Brewers Quay is a converted Victorian brewery near the Old Harbour in Weymouth, Dorset, southern England.  It was formerly the Devenish Brewery and then was an indoor shopping complex with around twenty specialty shops together with heritage and science exhibits, until it was closed in 2010.  From 2013-17, the building housed an antiques emporium.  It currently awaits redevelopment.

Castellammare del Golfo: Castellammare del Golfo (Sicilian: "Casteddammari" ; Latin: "Emporium Segestanorum" / "Emporium Aegestensium" ) is a town and "comune" in the Trapani Province of Sicily.  The name can be translated as "Sea Fortress on the Gulf", stemming from the medieval fortress in the harbor.  The nearby body of water conversely takes its name from the town, and is known as Gulf of Castellammare.

Megan Fox: Megan Denise Fox (born May 16, 1986) is an American actress and model.  She began her acting career in 2001, with several minor television and film roles, and played a regular role on the "Hope & Faith" television sitcom.  In 2004, she made her film debut with a role in the teen comedy "Confessions of a Teenage Drama Queen".  In 2007, she co-starred as Mikaela Banes, the love interest of Shia LaBeouf's character, in the blockbuster action film "Transformers", which became her breakout role.  Fox reprised her role in the 2009 sequel, "".  Later in 2009, she starred as the eponymous lead in the black comedy horror film "Jennifer's Body".

Jennifer Rothschild: Jennifer Rothschild (born 1963) is an American author and speaker.  She has written over 11 books and Bible studies, including the bestsellers, "Lessons I Learned in the Dark", "Self-Talk, Soul-Talk", and "Invisible: How You Feel is Not Who You Are".  Jennifer is the founder of "WomensMinistry.Net", a member based website that provides resources for women in leadership and equips them to lead well.  She is also the founder of "Fresh Grounded Faith", a national Christian women’s conference.  She has appeared on Good Morning America, Dr. Phil, The Learning Channel, Life Today, and a Billy Graham television special and spoken for Women of Faith and Extraordinary Women.  Jennifer regularly travels and speaks around the country, sharing her story with thousands of women.  She and her husband Phil have two sons and live in Missouri.

Faith branding: Faith branding is the concept of branding religious organizations, leaders, or media programming, in the hope of penetrating a media-driven, consumer-oriented culture more effectively.  Faith branding treats faith as a product and attempts to apply the principles of marketing in order to "sell" the product.  Faith branding is a response to the challenge that religious organizations and leaders face regarding how to express their faith in a media-dominated culture.

Question: What actress on Hope & Faith and in Jennifer's Body regularly shops at Nigel Beauty Emporium?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "tv_show_acted_in": {
      "type": "string",
      "description": "The name of the television show the actress regularly appeared in."
    },
    "movie_starred_in": {
      "type": "string",
      "description": "The name of the movie the actress starred in."
    },
    "beauty_emporium_name": {
      "type": "string",
      "description": "The name of the beauty supply store."
    },
    "emporium_client_status": {
      "type": "string",
      "description": "Description of the actress's association with the beauty emporium."
    }
  },
  "required": [
    "actress_name",
    "tv_show_acted_in",
    "movie_starred_in",
    "beauty_emporium_name",
    "emporium_client_status"
  ],
  "additionalProperties": false
}
