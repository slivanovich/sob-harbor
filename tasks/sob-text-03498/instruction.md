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
Proud Boys: Proud Boys is a far-right men's organization founded in 2016 by Vice Media co-founder and former commentator Gavin McInnes.  McInnes describes the organization as a "pro-Western fraternal organization" for men who "refuse to apologize for creating the modern world."  The group has been referred to as alt-right or alt-lite.

Creative Control (film): Creative Control is a 2015 American-French drama science-fiction film, directed by Benjamin Dickinson from a screenplay written by Micah Bloomberg and Dickinson.  It stars Dickinson, Nora Zehetner, Dan Gill, Alexia Rasmussen, Gavin McInnes and Reggie Watts.  The film had its world premiere at South by Southwest on March 14, 2015.  It was released on March 11, 2016, by Amazon Studios and Magnolia Pictures.

Gavin McInnes: Gavin Miles McInnes ( ; born 17 July 1970) is a Canadian writer, actor, comedian, co-founder of Vice Media and "Vice Magazine" and host of "The Gavin McInnes Show" on Compound Media.  He is a contributor for The Rebel Media and "Taki's Magazine", and was a frequent guest on television programs on Fox News and TheBlaze.  McInnes has been called "the Godfather of the Hipster movement" and "one of hipsterdom's primary architects".

Missbehave: Missbehave ia a Brooklyn-based women's magazine that was produced from 2006 until March 2009.  It covered fashion, music, art and pop culture.  Columnists included Kelis, Matt Goias, Gavin McInnes, Sarah Morrison and Lesley Arfin and regularly featured models Kim Matulova, Victoria Brito, Joli Robinson and Brissi.

Mother of All Rallies: The Mother of All Rallies (M.O.A.R.) was a rally held on September 16, 2017, at the National Mall in Washington, D.C., United States, in support of President Donald Trump.  The event was held on the same day as other demonstrations throughout the city, including the Juggalo March.  Speakers included Marco Gutierrez and the leaders of Gays for Trump and Patriot Prayer, among others.  Members of the 3 Percenters, American Guard, Oath Keepers, and Proud Boys were present, as were Antifa and Black Lives Matter activists.  Crowd estimates ranged from several hundred to around 1,000 attendees, far less than organizers' original goal of 1 million participants and claims that thousands would attend.  No Republican elected officials attended the rally.

Fightland: Fightland is a website covering mixed martial arts (MMA).  Launched in September 2012, it is part of Vice Media, Inc. network channels.  Vice Media states that "Fightland" is a joint venture with the Ultimate Fighting Championship (UFC). " The New Yorker" describes it as a vertical in which the UFC is sponsoring the whole website, and in general, concludes that "Vice’s sponsored material can feel like a strange beast, neither advertising nor regular content but something in between."

Viceland: Viceland (stylized as VICELAND) is a multinational brand of television channel owned by Vice Media, which also provides programming.  Viceland launched on February 29, 2016 with the simultaneous launch of two Viceland-branded cable channels; the American version (rebranded from H2) is a joint venture majority-owned by A&E Networks (who owns a 10% stake in Vice Media, alongside a separate 10% stake owned directly by A&E's co-owner Disney), while the Canadian version (rebranded from Bio) operates as a Category A-licensed specialty channel majority-owned by Rogers Media.

Compound Media: Compound Media (formerly The Anthony Cumia Network) is a subscription-based on-demand streaming media platform that broadcasts live American audio and video podcasts.  It launched on August 4, 2014 by its founder, radio personality and broadcaster Anthony Cumia, who began hosting "The Anthony Cumia Show" on the network after his firing from SiriusXM.  Since its launch, the network has grown to host additional shows, including those hosted by Pat Dixon, Dave McDonald, and Gavin McInnes.  In 2016, the network relaunched as Compound Media.

KACH: KACH (1340 AM) is a radio station broadcasting an Adult Contemporary format to the Preston, Idaho, United States, area.  The station is currently owned by Anthony Cumia and Gavin McInnes and features programing from Citadel Media.

Vice Media: Vice Media LLC is a North American digital media and broadcasting company.  Originating from the Montreal-based "VICE" magazine co-founded by Suroosh Alvi, Shane Smith, and Gavin McInnes (who left the company in 2008), VICE expanded primarily into youth and young adult–focused digital media, including online content verticals and related web series, the news division Vice News, a film production studio, and a record label among other properties.  In 2015 VICE Media was called "[arguably] a poster child for new-media success—especially when it comes to attracting a valuable millennial audience."

Question: Which far-right men's organization founded in 2016 by Vice Media co-founder and former commentator Gavin McInnes was present at the Mother of All Rallies (M.O.A.R.)?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "organization_name": {
      "type": "string",
      "description": "The name of the far-right men's organization."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the organization was founded."
    },
    "founder": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the founder."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key roles held by the founder mentioned in the context."
        }
      },
      "required": [
        "name",
        "roles"
      ],
      "additionalProperties": false
    },
    "rally_attendance": {
      "type": "object",
      "properties": {
        "rally_name": {
          "type": "string",
          "description": "The name of the rally where the organization was present."
        },
        "rally_date": {
          "type": "string",
          "description": "The date the rally was held."
        },
        "was_present": {
          "type": "boolean",
          "description": "Indicates if the organization was present at the rally."
        }
      },
      "required": [
        "rally_name",
        "rally_date",
        "was_present"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "organization_name",
    "founding_year",
    "founder",
    "rally_attendance"
  ],
  "additionalProperties": false
}
