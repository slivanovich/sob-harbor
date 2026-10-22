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
National Trust for Nature Conservation: The National Trust for Nature Conservation (NTNC), (राष्ट्रिय प्रकृति संरक्षण कोष) previously known as King Mahendra Trust for Nature Conservation is a Nepalese non-governmental organization working in the field of nature conservation. It was established in 1982 as an autonomous non profit organization by legislative law of Nepal.  NTNC's mission is to conserve nature and natural resources in Nepal while meeting the needs of the people in sustainable way.  Geographically, the Trust activities have spread from the sub-tropical plains of Chitwan, Bardia and Kanchanpur in the lowlands to the Annapurna and Manaslu region of the high Himalayas, including the trans-Himalayan region of Upper Mustang and Manang.  Currently, the projects of Trust are divided into three geographical areas - the lowland, the mid-hills (Kathmandu Valley) and the high mountains.  The Trust’s activities in the lowlands are based in and around the Chitwan National Park, the Bardia National Park and the Shuklaphanta Wildlife Reserve located in the central, western and far-western development regions of Nepal, through the Biodiversity Conservation Center (BCC) in Chitwan, the Bardia Conservation Program (BCP) in Bardia and the Suklaphanta Conservation Program (SCP) in Kanchanpur.  Similarly, the Annapurna Conservation Area Project (ACAP), the Manaslu Conservation Area Project (MCAP) and Gaurishankar Conservation Area Project (GCAP) are three protected areas managed by the Trust in the mountain region.  The Central Zoo is the only project of the Trust in Kathmandu Valley.  As a new initiative, the Trust has established an Energy and Climate Change Unit to address the emerging issues of climate change through mitigation and adaptation approach and renewable energy technologies.  The Trust has also started work on urban environment conservation with the Bagmati River Conservation Project.

Ghana Wildlife Society: The Ghana Wildlife Society is a conservationist NGO seeking to support Ghana's diverse wildlife to help provide both a "better environment" and an "improved quality of life for all people."  It is BirdLife International's partner in Ghana.  The society was formed in the early 1970s but suffered from a hiatus in its activities.  It was restarted in 1991 through a "Save the Seashore Birds Project - Ghana (SSPC-G)".  This project ended in June 1994 and the Society took over the work of that project.  The Society is involved with many conservation projects including: the Important Bird Areas Project-Ghana, the Amanzuri Community Integrated Project, the Mount Afadjato Community Forest Conservation Project, the Wetlands and Waterbird Conservation Project, the Conservation Awareness Programme in schools and communities, and the Marine Turtle Conservation Programme.  The projects are supported by a range of overseas donors including: Royal Society for the Protection of Birds, the UNDP and the Royal Netherlands Embassy in Ghana.

Hereford Screen: The Hereford Screen is a great choir screen designed by Sir George Gilbert Scott (1811–1878) and made by Coventry metalworking firm Skidmore & Co. for Hereford Cathedral, England in 1862.  It was one of the Gothic Revival works in iron of the nineteenth century.  When it was unveiled at the 1862 International Exhibition it was hailed as the "grandest and most triumphant achievement of modern architectural art".  Weighing over eight tonnes, the screen is a mixture of wrought and cast iron, brass, copper, semi-precious stones, and mosaics, supporting electroformed statues of Christ and attendant angels.  In 1967 the screen was dismantled as it was no longer considered fashionable.  The Victoria and Albert Museum acquired the screen in 1984, but it was in very poor condition.  In 2001, after a successful campaign to fund the largest conservation project ever undertaken by the Museum, the fully restored metal masterpiece was erected in pride of place, overlooking the main entrance.

Value America: Value America or VA was a dot-com company founded in Nevada in 1996 by Craig Winn and Rex Scatena, and relocated to Charlottesville, Virginia in February 1998.  Its business model involved connecting customers on the Web directly to manufacturers, with the intent of providing better pricing and faster shipping (a just-in-time model similar to those used by Wal-Mart and Dell).  Customers could order a wide range of products from VA's website, then VA would transmit the orders directly to the manufacturers, and the manufacturers would then package the products and ship them directly to the customer.  Winn referred to this concept as "convergence commerce".  Value America was backed by Microsoft co-founder Paul Allen's Vulcan Ventures and FedEx co-founder Frederick W. Smith.

Vulcan Inc.: Vulcan Inc. is a private company founded by philanthropist and investor Paul Allen.  It was established in 1986 and oversees Allen's diverse business activities and philanthropic endeavors--from sports teams which include the Seattle Seahawks and the Portland Trail Blazers to conservation projects such as the Great Elephant Census, the Seattle Cinerama, and Museum of Pop Culture.

Okapi Conservation Project: The Okapi Conservation Project OCP was founded in 1987 for the protection of the okapis ("Okapia johnstoni") and their habitat.  The okapi are only found in the Democratic Republic of Congo and are seen as the major flagship species of the Ituri Forest.  The OCP has about one hundred staff members and one hundred and ten government rangers under the direction of the Institute in Congo for the Conservation of Nature.  The Okapi Conservation Project is partnered with the Wildlife Conservation Network OCP's founder John Lukas is also a founding member of the Wildlife Conservation Network.  In 1992 the project helped create the Okapi Wildlife Reserve, encompassing 13,700 square kilometers of the Ituri Forest and in 1996, it was designated as a United Nations World Heritage Site.

Shapwick Heath: Shapwick Heath is a 394.0-hectare (973.6 acre) biological Site of Special Scientific Interest and national nature reserve between Shapwick and Westhay in Somerset, notified in 1967.  It is part of the Brue Valley Living Landscape conservation project.  The project commenced in January 2009 and aims to restore, recreate and reconnect habitat.  It aims to ensure that wildlife is enhanced and capable of sustaining itself in the face of climate change while guaranteeing farmers and other landowners can continue to use their land profitably.  It is one of an increasing number of landscape scale conservation projects in the UK.

Cayman Turtle Farm: Cayman Turtle Centre is a conservation facility and tourist attraction located in the West Bay district of the Cayman Islands.  It is used for raising the endangered Green Sea Turtle.  Established in 1968 by a group of American and British investors as "Mariculture Limited", the centre was initially a facility used to raise the Green Sea Turtle for commercial purposes.  By raising the turtle in a farming operation, the investors could raise turtle-meat for consumption without depleting the wild population of the species.  Still in operation as a farm that breeds and raises turtles in order to sell product, the Cayman Turtle Farm has also become a research centre and tourist attraction.  Currently, the centre is a conservation project as well as the largest land-based attraction in the Cayman Islands.  The turtle centre welcomes more than 500,000 visitors annually.

Brooklands Trust Members: Brooklands Trust Members (BTM) are the official support group for Brooklands Museum in Weybridge, Surrey, England.  It is governed by a charitable trust.  The BTM's main aims are to financially support and promote Brooklands Museum.  Principally funds are raised for the Museum through subscriptions to the BTM and by additional fund raising activities throughout the year such as an annual Classic Car Show & Jumble, a series of popular talks and other events The BTM also fund specific projects such as the restoration of the Pratts petrol pagoda which was opened in October 2010 by HRH Prince Michael of Kent and the replacement of the Test Hill railings.

Solzhenitsyn Aid Fund: The Solzhenitsyn Aid Fund (officially Russian Public Fund to Aid Political Prisoners and their Families, also Fund for the Aid of Political Prisoners, Public Aid Fund) was a charity foundation and support network set up by Aleksandr Solzhenitsyn and Alexander Ginzburg that distributed funds and material support to political and religious prisoners across the Soviet Union throughout the 1970s and 1980s.

Question: What "Census" conservation project did the group that backed Value America also fund?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "project_name": {
      "type": "string",
      "description": "The name of the conservation project."
    },
    "project_type": {
      "type": "string",
      "description": "The type of project, e.g., 'conservation'."
    },
    "funding_entity": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the entity that funded the project."
        },
        "founder": {
          "type": "string",
          "description": "The founder of the funding entity."
        }
      },
      "required": [
        "name",
        "founder"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "project_name",
    "project_type",
    "funding_entity"
  ],
  "additionalProperties": false
}
