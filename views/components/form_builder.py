import customtkinter as ctk


class FormBuilder:

    @staticmethod
    def create_form(parent, fields):

        widgets = {}

        form = ctk.CTkFrame(parent)
        form.pack(fill="both", expand=True, padx=20, pady=20)

        row = 0

        for field in fields:

            label_text = field[0]
            field_type = field[1]

            label = ctk.CTkLabel(
                form,
                text=label_text
            )

            label.grid(
                row=row,
                column=0,
                padx=15,
                pady=10,
                sticky="w"
            )

            if field_type == "entry":

                widget = ctk.CTkEntry(
                    form,
                    width=300
                )

            elif field_type == "combo":

                widget = ctk.CTkComboBox(
                    form,
                    width=300,
                    values=field[2]
                )

                widget.set(field[2][0])

            widget.grid(
                row=row,
                column=1,
                padx=15,
                pady=10,
                sticky="w"
            )

            widgets[label_text] = widget

            row += 1

        return widgets