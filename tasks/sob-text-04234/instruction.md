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
The Surfer's Path: The Surfer's Path was a bi-monthly international surfing magazine founded by Alex Dick-Read.  The magazine was established in 1997 as part of the Permanent Publishing stable (alongside "Whitelines Snowboard Magazine" and "Sidewalk Skateboard Magazine").  The headquarters was originally in Cornwall.  It was then owned by Factory Media and had its headquarters in London, England.  From 2004 it was published on recycled paper.  An American edition of the magazine was edited by Drew Kampion.  "The Surfer's Path" closed its doors in January 2014.

Prairie Mountain Publishing: The Prairie Mountain Publishing Company is an American publishing company owned by Digital First Media.  Former half owner Scripps left the partnership in 2009.

Blunt (snowboard magazine): Blunt Snowboard Magazine was an American snowboard magazine published in the 1990s.  The magazine was established in 1993 and the founder was Ken Block.  DC Shoes were the initial publishers of "Blunt", which mainly featured advertisements for new, small and independent companies.  The magazine also featured regular submissions by skateboarder Ed Templeton and photos by Rob "Whitey" McConnaughy.  The magazine was eventually sold to "Big Brother Magazine" and in 1997 on to Larry Flynt Publications who discontinued it a few years later.

XXL (magazine): XXL is an American hip hop magazine, published by Townsquare Media, founded in 1997.

Snowboard Magazine: Snowboard Magazine is an independent snowboarding publication.  It was founded in April 2004 by Mark Sullivan and Liz Sullivan in Hailey, Idaho.  Soon they were joined by Jeff Baker, Aaron Draplin, Gary Hansen and Jason "J2" Rasmus.  Most of the crew were previous employees and/or contracted employees of "Snowboarder Magazine".  Until 2007 Mark Sullivan was also the publisher.  The magazine was the first product focused magazine in snowboarding, quickly set trends for competing titles to follow and quickly became the third largest snowboarding publication in the world.  In 2011 "Snowboard Magazine" was sold to Storm Mountain Publishing, publishers of "Freeskier Magazine", which is based in Boulder, Colorado.

Low Island, Falkland Islands: Low Island is one of the Falkland Islands and is the birthplace of businessman James Lowis.  It is near West Falkland, to its north, in Byron Sound It is between Carcass Island and Dunbar Island and to the west of Saunders Island.  It is south of Sedge Island and north of the Byron Heights and Storm Mountain.

Storm Mountain (Alberta): Storm Mountain is a mountain in Alberta's Rockies, Canada.

Carrabassett Valley Academy: Carrabassett Valley Academy is a private ski and snowboard academy offering most downhill winter mountain sports.  Carrabassett Valley Academy is based in Carrabassett Valley, Maine at the base of Sugarloaf Mountain.  Established in 1982, the school has trained and schooled the likes of Olympic competitors Bode Miller, Seth Wescott, Kirsten Clark, and Emily Cook.  Jeremy Jones, nine-time Snowboard Magazine Big Mountain Rider of the Year, also honed his snowboarding and academic skills at Carrabassett Valley Academy.  Since 1982 CVA has produced 12 Olympians, 92 National Titles, 11 X-Games competitors, 26 NCAA and USCSA All-Americans, 39 national team members, and six world champions.

Arashiyama: Arashiyama (嵐山 , Storm Mountain ) is a district on the western outskirts of Kyoto, Japan.  It also refers to the mountain across the Ōi River, which forms a backdrop to the district.  Arashiyama is a nationally designated Historic Site and Place of Scenic Beauty.

Split Island, Falkland Islands: Split Island is one of the Falkland Islands.  It is near West Falkland, to its west, at the mouth of King George Bay.  It is to the west of Rabbit Island, Hummock Island and Middle Island.  It is north of the Passage Islands and south east of Westpoint Island, and south west of the Byron Heights and Storm Mountain.

Question: In between XXL and Snowboard Magazine,which one was sold was sold to Storm Mountain Publishing?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_sold": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the magazine that was sold."
        },
        "type": {
          "type": "string",
          "description": "The type or genre of the magazine."
        },
        "year_founded": {
          "type": "integer",
          "description": "The year the magazine was founded."
        }
      },
      "required": [
        "name",
        "type"
      ],
      "additionalProperties": false
    },
    "acquiring_company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the company that acquired the magazine."
        },
        "location": {
          "type": "string",
          "description": "The headquarters location of the acquiring company."
        }
      },
      "required": [
        "name",
        "location"
      ],
      "additionalProperties": false
    },
    "year_of_sale": {
      "type": "integer",
      "description": "The year the magazine was sold to the acquiring company."
    }
  },
  "required": [
    "magazine_sold",
    "acquiring_company",
    "year_of_sale"
  ],
  "additionalProperties": false
}
