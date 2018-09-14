from binaryninja_cortex.platforms import MCU

class Chip(MCU):
    NAME="LPC43XX_M0"
    ROM_OFF=0x1A000000 
    RAM_OFF=0x10000000 

    IRQ=MCU.IRQ+ [
        "NVIC_USART0_IRQ",
        "NVIC_UART1_IRQ",
        "NVIC_USART2_OR_C_CAN1_IRQ",
        "NVIC_USART3_IRQ",
        "NVIC_SPI_OR_DAC_IRQ",
        "NVIC_ADC1_IRQ",
        "NVIC_SSP0_OR_SSP1_IRQ",
        "NVIC_EVENTROUTER_IRQ",
        "NVIC_I2S0_OR_I2S1_IRQ",
        "NVIC_C_CAN0_IRQ",
        "NVIC_M4CORE_IRQ",
        "NVIC_RTC_IRQ",
        "NVIC_DMA_IRQ",
        "NVIC_ETHERNET_IRQ",
        "NVIC_FLASHEEPROMAT_IRQ",
        "NVIC_LCD_IRQ",
        "NVIC_SDIO_IRQ",
        "NVIC_USB1_IRQ",
        "NVIC_USB0_IRQ",
        "NVIC_RITIMER_OR_WWDT_IRQ",
        "NVIC_SCT_IRQ",
        "NVIC_GINT1_IRQ",
        "NVIC_TIMER0_IRQ",
        "NVIC_TIMER3_IRQ",
        "NVIC_PIN_INT4_IRQ",
        "NVIC_ADC0_IRQ",
        "NVIC_MCPWM_IRQ",
        "NVIC_SGPIO_IRQ",
        "NVIC_I2C0_OR_IRC1_IRQ",
        ]
