from datetime import datetime
today = datetime.today().strftime('%Y-%m-%d')
pe_id = int(input("project euler id = "))

template=f"""---
title: "Project Euler {pe_id} : 
date: {today}
author: "Aditya Kumar Singh"
description: "Project Euler: hint and solution to problem {pe_id}"
tags: [
  "project-euler"
]
categories: [
  "project-euler"
]
---

Link to official statement : [TODO](https://projecteuler.net/problem={pe_id})


## Hints

## Source Code

{{{{<details-open Haskell>}}}}

```haskell
todo
```

Checkout solution at [Github](https://github.com/poincareGYP/project-euler/blob/main/solution/{pe_id}.hs)

{{{{<details-close>}}}}

"""

with open(f"project-euler-{pe_id}.md", "w") as f:
    f.write(template)

