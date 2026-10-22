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
American whiskey: American whiskey is a distilled beverage produced in the United States from a fermented mash of cereal grain.  Among the types included under this designation are bourbon whiskey, rye whiskey, rye malt whiskey, malt whiskey, wheat whiskey, and corn whiskey.  All of these are made from mashes with at least 51% of their named grains.

American Trilogy Cocktail: The American Trilogy cocktail is a variation of the classic Old Fashioned.  Barmen Richard Boccato and Michael McIlroy, created the American Trilogy in 2007 while bartending together at New York’s Little Branch.  This Old Fashioned-style cocktail follows the same bitters, sugar, whiskey and orange peel profile as the classic, but uses orange bitters, a brown sugar cube and one part Applejack and one part rye whiskey to change it up.  As the name implies, each ingredient of this three-part cocktail represents one pillar of the Trilogy.  Laird’s Bonded Applejack Brandy is the first and oldest distilled spirit in America with American rye whiskey following soon after in the late 1700s.  The third pillar of this cocktail is somewhat of a mystery according to creator Richard Boccato, but is often thought to be the orange bitters because of its American Origins.

Cachaça: Cachaça (] ) is a distilled spirit made from fermented sugarcane juice.  Also known as "aguardente", "pinga", "caninha" and other names, it is the most popular spirit among distilled alcoholic beverage in Brazil.  Outside Brazil, cachaça is used almost exclusively as an ingredient in tropical drinks, with the "caipirinha" being the most famous cocktail.

Heaven Hill: Heaven Hill Distilleries, Inc. is an American, private family-owned and operated distillery company headquartered in Bardstown, Kentucky that produces and markets the Heaven Hill brand of Kentucky Straight Bourbon Whiskey and a variety of other distilled spirits.  Its current distillery facility, called the Heaven Hill Bernheim distillery, is in Louisville, Kentucky.  It is the seventh-largest alcohol supplier in the United States, the second-largest holder of bourbon whiskey inventory in the world, the largest independent family-owned and operated producer and marketer of distilled spirits in the United States, and the only large family-owned distillery company headquartered in Kentucky (not counting the Brown-Forman Corporation, which is publicly traded but more than two-thirds family-controlled, or the Sazerac Company, which is family-owned but headquartered in Louisiana).

Trying to Be Cool: "Trying to Be Cool" is a song by the French band Phoenix from their fifth album "Bankrupt! ".  It was released as the second single from the album on July 8, 2013.  The official remix features R. Kelly.  The song became Phoenix's third top-ten hit on the "Billboard" Alternative Songs chart, after "1901" and "Lisztomania".  The song's cover includes a mint julep, which is said in one of the song's lines, "mint julep testosterone".  Frontman Thomas Mars told "Spin" magazine the lyrics to "Trying to Be Cool" mainly analyze "the beauty of the fake".

Whiskey Rebellion: The Whiskey Rebellion (also known as the Whiskey Insurrection) was a tax protest in the United States beginning in 1791 during the presidency of George Washington.  The so-called "whiskey tax" was the first tax imposed on a domestic product by the newly formed federal government.  It became law in 1791, and was intended to generate revenue for the war debt incurred during the Revolutionary War.  The tax applied to all distilled spirits, but American whiskey was by far the country's most popular distilled beverage in the 18th century, so the excise became widely known as a "whiskey tax".  Farmers of the western frontier were accustomed to distilling their surplus rye, barley, wheat, corn, or fermented grain mixtures into whiskey.  These farmers resisted the tax.  In these regions, whiskey often served as a medium of exchange.  Many of the resisters were war veterans who believed that they were fighting for the principles of the American Revolution, in particular against taxation without local representation, while the federal government maintained that the taxes were the legal expression of Congressional taxation powers.

Mint julep: The mint julep is a mixed alcoholic drink, or cocktail, consisting primarily of bourbon (or some other spirit), water, crushed or shaved ice, and fresh mint.  As a bourbon-based cocktail, it is associated with the American South and the cuisine of the Southern United States in general, and the Kentucky Derby in particular.

Willett Pot Still Reserve: Willett Pot Still Reserve Bourbon is brand of a bourbon whiskey produced in Bardstown, Kentucky by the Willett Distillery.  It is a Kentucky straight bourbon whiskey brand introduced in 2008 and bottled at 47% abv, with 8–10 year aging.  It is sold in glass 750 ml and 1.75 liter bottles.  The company is identified on the product label as the Willett Distilling Company, which was the original name of the company until its name was changed in 1984 to Kentucky Bourbon Distillers, Ltd. (KBD).  In October 2012, the company announced that it would return to using the Willett name as its primary business name.  Recent bottlings are identified on the labels as a small batch bourbon, whereas it was originally released as a single barrel bourbon.

Cougar Bourbon: Cougar bourbon whiskey, formerly called Sam Cougar's, is a brand of bourbon whiskey produced in Lawrenceburg, Indiana.  It is an export-only brand owned by Foster's Group (a division of SABMiller) that is bottled and sold in Australia and New Zealand, where it is a popular bourbon whiskey.  It is sold at 37% alc. /vol.

Bourbon whiskey: Bourbon whiskey is a type of American whiskey, a barrel-aged distilled spirit made primarily from corn.  The name is derived from the French Bourbon dynasty, although it is unclear precisely what inspired the whiskey's name (contenders include Bourbon County in Kentucky and Bourbon Street in New Orleans).  Bourbon has been distilled since the 18th century.  The use of the term "bourbon" for the whiskey has been traced to the 1820s, and the term began to be used consistently in Kentucky in the 1870s.  While bourbon may be made anywhere in the United States, it is strongly associated with the American South, and with Kentucky in particular.  As of 2014, the distillers' wholesale market revenue for bourbon sold within the U.S. is about $2.7 billion, and bourbon makes up about two-thirds of the $1.6 billion of U.S. exports of distilled spirits.

Question: The mint julep is a mixed alcoholic drink, or cocktail, consisting primarily of Bourbon whiskey, a whiskey of which nationality, a barrel-aged distilled spirit made primarily from corn?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cocktail_name": {
      "type": "string",
      "description": "The name of the mixed alcoholic drink."
    },
    "primary_spirit_ingredient": {
      "type": "string",
      "description": "The main spirit ingredient of the cocktail."
    },
    "spirit_nationality": {
      "type": "string",
      "description": "The country of origin or nationality of the primary spirit."
    },
    "spirit_characteristics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key characteristics describing the primary spirit."
    }
  },
  "required": [
    "cocktail_name",
    "primary_spirit_ingredient",
    "spirit_nationality",
    "spirit_characteristics"
  ],
  "additionalProperties": false
}
