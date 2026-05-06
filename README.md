# Dead Stock Analysis — FMCG Storage

## Problem
  
In retail, the assumption that the loop, import - storage - sell, is a wrong assumption. Products get misplaced, stolen, hidden, damaged, lost... is a ever present problem. This dataset will paint a broad picture of how dead stock accumulates in a real FMCG storage environment, and why reported inventory numbers rarely match what's physically on the shelf.

## Data

This database is a simulated report of a small retail store, specifically in the FMCG section. Within this is 500 SKUs of various brands, product categories and types.

The criteria to flag a product as "dead stock" is if the days since last import exceeds 180.

Data was simulated based on firsthand observation working in FMCG storage, as real inventory data was locked within a proprietary company system.

## Findings

Analysis of 500 SKUs across 5 product categories revealed the following:

  By SKUs:
  
  - Active: 248
  - Slow moving: 83
  - Dead stock: 169

  By units:
  
  - Active: 56632
  - Slow moving: 19577
  - Dead stock: 128439

  By number of units in categories:
  
  - Milk: 38793
  - Soft drink: 37888
  - Instant noodle: 18280
  - Candy: 17263
  - Cooking oil: 16215

  Space waste:
  Wasted units (dead + slow): 148016
  Wasted percentage: 72.3%

## Insights

The data showed that dead stock and slow moving product have quite a significant percentage both in number and in storage space wastage. The reason behind these findings are multiple and layered.

The first reason is inefficient storage work. Products that are literally in the store, but are hidden behind layers of stocks, making a self-reinforcing loop. As old products are not consumed, new products keep coming in, and hide the already available stocks. This can also lead to the second reason, damaged goods. As stocks are in storage for a long time, pests can get inside the products, spoiling and damaging it as the same time, making consumption unavailable, and storage tracking harder.

The third reason can be attributed to theft. Inside a retail environment, that have a lot of foot traffic, theft is common. Staffs can't observe all customers, whether intentional or not.

There is a cause that is less common, but can make the store underreport the available stock, that is when a product was sold, but not registered. This is common in rush hour, when the customers exceed the capacity of help, and mistracking/miscanning can happen.

The last reason, and the least expected, can be attributed to neglection. Whether due to understaffing, overworking or simply lack of accountability to keep a consistent report of real stock.

## Recommendations

The solution is a multi-pronged and requires commitment.

First, the storage must be organized in such a way that is systematic, sorted by type and category. There should be enough white space to store new shipment on demand, otherwise new boxes will have to store in the pathway, which is detrimental for sales and revenue.

Cameras should cover all areas, to effectively determine the reason for missing products, and keep a timeline for missing ones.

Staffing is another area that must be adequately solved. Staffs shouldn't be working more than 10 hours a day, to keep a high morale and productivity. The store should have enough headcount to cover all shifts, and have a overlapping time schedule so that they can be present at all times. Managers and leaders should be competent enough to overseeing accoutability is accurately assigned.

Finally, the store should implement a basic inventory tracking system that flags products with no import activity beyond 90 days, giving management early warning before dead stock accumulates.
