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
Cape Horn Biosphere Reserve: The Cape Horn Biosphere Reserve (Cabo de Hornos Biosphere Reserve) is located in the extreme south of Chile and comprises marine areas, islands, fjords, channels, forests and moorland.  It covers an area of approximately 49000 km2 .  All biosphere reserves include core zones (no significant infrastructure development), buffer zones (light development) and transition zones (more traditional development under a sustainable rubric).  In the case of Cape Horn Biosphere Reserve, the core zone is constituted of Alberto de Agostini National Park and Cabo de Hornos National Park, which are strictly protected under Chilean law and under the biosphere reserve status cannot have infrastructure for lodging.

Ciénaga de Zapata Biosphere Reserve: The Ciénaga de Zapata Biosphere Reserve (established 2000) is a UNESCO Biosphere Reserve situated on the southern coast of Cuba at Matanzas province.  The 628,171 ha reserve encompasses the Zapata Swamp and is one of the largest and most important wetlands in the Caribbean region with a marine southern borderline.  Ciénaga de Zapata was designated a Ramsar site in 2001.  This area is a cluster biosphere reserve with several core areas, highly valuable for conservation located in the Ciénaga de Zapata National Park.

Noosa Biosphere Reserve: Noosa Biosphere Reserve is an internationally protected area covering the region of Noosa in Queensland, Australia.  It is formally recognised as a Biosphere Reserve by the United Nations Education, Scientific and Cultural Organisation (UNESCO) and Man and the Biosphere (MAB) program for its highly diverse ecosystem over a relatively small space.  It was the first Biosphere Reserve for the state of Queensland, established in September 2007.  The reserve is bound by the former Noosa Shire Council boundaries, extending offshore by 3 km , covering 150000 ha in total.  It is governed by Noosa Biosphere Limited (NBL), a not-for-profit company, which mainly consists of members from the local community who fulfil roles in the governance board, sector boards, and partnerships.  Community plays a significant role in the implementation of the Biosphere Reserve guidelines.

San Guillermo National Park: San Guillermo National Park (Spanish: "Parque Nacional San Guillermo" ) is a national park in Argentina, in the Iglesia Department of San Juan Province.  It was established in 1999 and is part of the San Guillermo Biosphere Reserve.  The highest point of the biosphere reserve is about 6000 m .  It consists of grasslands, wetlands, and canyons.  The animals there include vicuña, guanaco, culpeo fox, Andean mountain cat, cougar, and Andean condor.

Andean mountain cat: The Andean mountain cat ("Leopardus jacobita") is a small wild cat native to the high Andes that has been classified as Endangered by IUCN because fewer than 2,500 individuals are thought to exist in the wild.

Southwest Nova Biosphere Reserve: The Southwest Nova Biosphere Reserve was designated in 2001 under the UNESCO Man and the Biosphere Programme.  The Southwest Nova Biosphere Reserve spans a total of 1.5 million hectares consisting of five counties in Nova Scotia, Canada: Annapolis, Digby, Queens, Shelburne and Yarmouth.  The core protected areas of the biosphere reserve are Kejimkujik National Park and the Tobeatic Wilderness Area.

Jornada Biosphere Reserve: The Jornada Biosphere Reserve (established 1976) is a UNESCO Biosphere Reserve in southern New Mexico.  It is one of three biosphere reserves representing the Chihuahuan Desert (along with Big Bend Biosphere Reserve and National Park in western Texas and Mapimí Biosphere Reserve in Mexico).  The area extends from the crest of the San Andres Mountains, which are dominated by shrub woodlands, to the Jornada Plains characterized by semi-desert grasslands.

Riding Mountain Biosphere Reserve: Riding Mountain Biosphere Reserve (RMBR) is a UNESCO World Biosphere Reserve designated by the United Nations Educational, Scientific and Cultural Organization (UNESCO) in 1986 as part of its Man and the Biosphere Programme.  The RMBR, which encompasses Riding Mountain National Park and twelve surrounding municipalities in the province of Manitoba, is one of 16 Biosphere Reserves in Canada.  Ecologically sensitive ecosystems include the grasslands, deciduous forest and boreal forest.  Although grasslands occupy only 7,400 of the total 1,331,800 hectares, they are considered of national importance since they exist as discrete units and the rare climax rough fescue community represents the eastern extent of its range.  The Biosphere Reserve extends the protection of these ecosystems outside of park boundaries.  Municipalities in the Riding Mountain Biosphere Reserve include Clanwilliam – Erickson, Dauphin, Gilbert Plains, Grandview, Harrison Park, Lakeshore, McCreary, Rosedale, St. Rose, Riding Mountain West, Rossburn, and Yellowhead.  First Nations in the Biosphere Reserve include Rolling River First Nation, Keeseekoowenin First Nation, Waywayseecappo First Nation, and Tootinaowaziibeeng First Nation.  Asessippi Provincial Park and Duck Mountain Provincial Forest also border the Biosphere Reserve.

Waterton Biosphere Reserve: Waterton Biosphere Reserve (established 1979) is a UNESCO Biosphere Reserve encompassing Waterton Lakes National Park in the extreme south-west of the Province of Alberta, Canada.  The reserve includes a section of the east slopes of the Rocky Mountains extending from the Continental Divide to the edge of the Canadian Great Plains to the east.  The Glacier Biosphere Reserve and National Park in Montana, USA is located to the south of the area.  The reserve is administered by Waterton Lakes National Park and the Waterton Biosphere Association. 

Mapimí Biosphere Reserve: The Mapimí Biosphere Reserve (Spanish: "Reserva de la Biósfera de Mapimí" ) (established 1977) is a UNESCO Biosphere Reserve located in the state of Durango in northern Mexico.  It is one of three biosphere reserves representing the Chihuahuan Desert (along with Big Bend Biosphere Reserve and National Park in western Texas and Jornada Biosphere Reserve in New Mexico).  The 342,388 ha reserve is situated between the Neotropical and Neartic biogeographical regions, in the Bolsón de Mapimí 1,150 m above sea level.  It contains three core areas in the "Sierra de la Campana", the "Laguna de las Palomas", a salt lagoon, and a desert habitat called "Dunas de la Soledad".  It comprises fragile warm desert and semi-desert ecosystems and rich, highly adapted but vulnerable plant systems, mainly xerophytic matorral scrub, and animal species such as the puma ("Puma concolor"), mule deer ("Odocoileus hemionus"), sandhill crane ("Grus canadensis") and the kit fox or "zorrita del desiert" ("Vulpes macrotis") along with scrub and desert grasslands.

Question: What small wild cat native to the high Andes that has been classified as Endangered by IUCN, lives in a national park established in 1999 and is part of the San Guillermo Biosphere Reserve?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "animal_name": {
      "type": "string",
      "description": "The common name of the animal."
    },
    "species_scientific_name": {
      "type": "string",
      "description": "The scientific name of the animal species."
    },
    "conservation_status": {
      "type": "string",
      "description": "The conservation status as classified by IUCN."
    },
    "population_estimate": {
      "type": "integer",
      "description": "Estimated number of individuals in the wild."
    },
    "habitat_details": {
      "type": "object",
      "properties": {
        "native_region": {
          "type": "string",
          "description": "The region where the animal is native."
        },
        "national_park": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the national park where the animal lives."
            },
            "establishment_year": {
              "type": "integer",
              "description": "The year the national park was established."
            }
          },
          "required": [
            "name",
            "establishment_year"
          ],
          "additionalProperties": false
        },
        "biosphere_reserve_name": {
          "type": "string",
          "description": "The name of the biosphere reserve that includes the national park."
        }
      },
      "required": [
        "native_region",
        "national_park",
        "biosphere_reserve_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "animal_name",
    "species_scientific_name",
    "conservation_status",
    "population_estimate",
    "habitat_details"
  ],
  "additionalProperties": false
}
