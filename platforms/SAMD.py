from binaryninja_cortex.platforms import MCU

class Chip(MCU):
    NAME="SAMD"
    ROM_OFF=0x00000000 
    RAM_OFF=0x20000000
    IRQ=MCU.IRQ+ [
        "NVIC_PM_IRQ",
        "NVIC_SYSCTRL_IRQ",
        "NVIC_WDT_IRQ",
        "NVIC_RTC_IRQ",
        "NVIC_EIC_IRQ",
        "NVIC_NVMCTRL_IRQ",
        "NVIC_DMAC_IRQ",
        "NVIC_RESERVED1_IRQ",
        "NVIC_EVSYS_IRQ",
        "NVIC_SERCOM0_IRQ",
        "NVIC_SERCOM1_IRQ",
        "NVIC_SERCOM2_IRQ",
        "NVIC_TCC0_IRQ",
        "NVIC_TC1_IRQ",
        "NVIC_TC2_IRQ",
        "NVIC_ADC_IRQ",
        "NVIC_AC_IRQ",
        "NVIC_DAC_IRQ",
        "NVIC_PTC_IRQ",
        ]
