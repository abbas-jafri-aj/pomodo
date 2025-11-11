import ttkbootstrap as ttk

class CustomMeter(ttk.Meter):
    def __init__(self, *args, **kwargs):
        # Optional: initial display text
        self._display_text = kwargs.pop("display_text", None)
        super().__init__(*args, **kwargs)

    @property
    def display_text(self):
        return self._display_text

    @display_text.setter
    def display_text(self, value):
        self._display_text = value
        self._update_display_text()

    def _update_display_text(self):
        """Update center text with display_text if set."""
        if self._display_text is not None:
            self.amountuseddisplayvar.set(str(self._display_text))
        else:
            # fallback to numeric value
            amount_used = self.amountusedvar.get()
            self.amountuseddisplayvar.set(self._amountformat.format(amount_used))

    def _update_meter(self, *_):
        """Override parent _update_meter to respect display_text."""
        # draw the meter as usual
        self._draw_meter()
        # update center text
        self._update_display_text()
