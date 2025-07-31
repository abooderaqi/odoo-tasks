## 🔗 Useful Links

- [Python Basics Cheat Sheet](https://www.pythoncheatsheet.org/cheatsheet/basics) – A handy reference for essential Python syntax and commands.
- [Learn By Example – Python](https://www.learnbyexample.org/python/) – A detailed guide covering Python concepts through examples.
- [Git Cheat Sheet (GitHub Education PDF)](https://education.github.com/git-cheat-sheet-education.pdf) – A printable cheat sheet covering essential Git commands and workflows.


___


# 🎯 Task Title 01: ![Done](https://img.shields.io/badge/status-done-brightgreen)

### Basic Python Task: https://github.com/abooderaqi/odoo-tasks/tree/task01

___

# 🎯 Task Title 02: ![Done](https://img.shields.io/badge/status-done-brightgreen)

### "Customize Workflow for Internal Purchase Request Approval"

## ✅ Task Description:
Create or modify a workflow for an Internal Purchase Request module so that it goes through a multi-step approval process before being fully approved.

The stages should be:

Draft – Initial state when the request is created.

Waiting for Manager Approval – The first approval step.

Waiting for Finance Approval – After the manager approves.

Approved – Final approval by the finance team.

## 🎯 Learning Objectives:
The intern should:

Understand how to use and manage state fields in models.

Create buttons that move the document from one state to another.

Add proper user access control (only managers can approve at one stage, and finance at the next).

Use groups and security XML properly.

Add chatter messages (message_post) to show activity.

Build a functional form and tree view.

Optionally, use sequences to auto-generate request references.

____


# 🎯 Task Title 03: ![Progress](https://img.shields.io/badge/status-in--progress-yellow)
### Collaborating with a Team Using Git & GitHub `(TechSkills)`

## ✅ Task Description:
Create a new Git branch named Task02 and push the code for Task 02 to that branch on GitHub. Follow Git best practices and provide all the commands you used during the process.

## 🧪 Deliverables:
A working branch on GitHub named Task02 containing Task 02 code.

A list of all Git commands used, written clearly below.

## 💻 Git Commands Used:
```bash

```

___

# 🎯 Task Title 04: ![New](https://img.shields.io/badge/status-new-blue)
### "Add Custom Field to Purchase Order & Transfer to Vendor Bill"
## ✅ Task Description:
Add a new custom field (e.g. `Purchase Purpose`) to both the Purchase Order and the Vendor Bill (Invoice).

The field should be filled in the Purchase Order, and when a Vendor Bill is created from the Purchase Order, the value should automatically transfer and appear in the Invoice.

add the field on `account.move` and on `purchase.order` on Form view And On List view


## 🎯 Learning Objectives:
Understand how to extend and inherit Odoo models.

Learn how to override default methods (especially the one creating vendor bills from purchases).

Gain experience working with form views and field visibility.

Reinforce skills in transferring data between related models.

## 🧪 Deliverables:
Updated module with the new field on Purchase and Invoice.

Value properly transferred when creating invoice from Purchase.

Code pushed to GitHub under a new branch named Task04.

___

# 🎯 Task Title 05: ![New](https://img.shields.io/badge/status-new-blue)

### "Add a Smart Button to View Related Invoices from Purchase Order"
## ✅ Task Description:
Create a smart button on the Purchase Order form view that shows all Vendor Bills (invoices) linked to that purchase order.

When clicked, the button should open a list view of the related `account.move` records (where the move type is `in_invoice` and the invoice is linked to that Purchase Order).


## 🎯 Learning Objectives:
Learn how to create smart buttons using Odoo form view XML.

Understand how to define custom actions and return views programmatically.

Practice using domain filters and relations between models.

## 🧪 Deliverables:
Smart button correctly placed on the Purchase Order form.

Clicking the button opens related Vendor Bills.

Count is displayed properly.

Code pushed to GitHub under a new branch named Task05.

___

# 🎯 Task Title 06: ![New](https://img.shields.io/badge/status-new-blue)

### "Create a Server Action to Update a Custom Field on Purchase Orders"
## ✅ Task Description:
Create a custom field (e.g., "Urgency Level" or "Internal Note") on the Purchase Order model. Then, build a Server Action that allows users to update this field to a specific value by selecting it from the Actions dropdown in the form view.

For example: Set "Urgency Level" to "High" when the Server Action is triggered.

## 🎯 Learning Objectives:
Learn how to create and modify fields dynamically via server actions.

Understand how to bind server actions to models and make them user-triggered.

Reinforce knowledge of using selection fields and Odoo automation.

## 🧪 Deliverables:
New field (urgency_level or similar) visible on Purchase Order form.

Server Action updates the field when triggered from the UI.

Code pushed to GitHub under a new branch named Task06.

___

# 🎯 Task Title 07: ![New](https://img.shields.io/badge/status-new-blue)

### "Create a New Model in Purchase Module and Load Data via XML"
## ✅ Task Description:
Create a new custom model under the Purchase module (e.g., purchase.tags or purchase.category) and pre-load some records into it using a data.xml file.

This task helps you practice creating standalone models and using XML data files for initial content.

## 🎯 Learning Objectives:
Learn how to define new models in Odoo.

Understand how to preload data using XML files.

Reinforce working with __manifest__.py and data file structure.

## 🧪 Deliverables:
A fully functional model under the Purchase module.

XML file (data.xml) with at least 3 records loaded on module install.

Code pushed to GitHub under a new branch named Task07.

___

# 🎯 Task Title 08: ![New](https://img.shields.io/badge/status-new-blue)
### "Use @api.depends and @api.onchange to Compute and Update Fields"
## ✅ Task Description:
Add a new field called total_product_qty (Float) to the Purchase Order model.

This field should compute the total quantity of all products in the order lines (order_line.product_qty).

Use @api.depends to automatically recompute this value when lines are added/modified.

Create another field called note_based_on_qty (Char).

Use @api.onchange to set a note dynamically:

If total quantity > 100 → note is "Large Order"

If between 50–100 → note is "Medium Order"

Else → note is "Small Order"

## 🎯 Learning Objectives:
Learn how to define computed fields using @api.depends.

Understand @api.onchange and how it differs from computed fields.

Practice logic branching in Python based on computed values.

Reinforce Odoo UI interaction using onchange updates.

## 🧪 Deliverables:
total_product_qty computed field correctly calculating quantity sum.

note_based_on_qty updated dynamically when lines are changed.

Fields are visible in the Purchase Order form view.

Code pushed to GitHub under a branch named Task08.
